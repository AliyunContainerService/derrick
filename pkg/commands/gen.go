package commands

import (
	"bytes"
	"embed"
	"encoding/json"
	"fmt"
	"io/fs"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
	"text/template"

	"github.com/Masterminds/sprig/v3"
	"github.com/mitchellh/mapstructure"
	"github.com/spf13/cobra"

	"github.com/alibaba/derrick/pkg/common"
	"github.com/alibaba/derrick/pkg/rigging"
	"github.com/alibaba/derrick/pkg/runtime"
	pkgtemplate "github.com/alibaba/derrick/pkg/template"
)

type genOption struct {
	Path       string
	ChosenRig  string
	TemplateFS embed.FS
}

func NewGenCommand(templateFS embed.FS) *cobra.Command {
	o := &genOption{
		TemplateFS: templateFS,
	}
	cmd := &cobra.Command{
		Use:     "gen",
		Short:   "Inspect the application and generate Dockerfile",
		Example: `derrick gen`,
		RunE: func(cmd *cobra.Command, args []string) error {
			return o.Run()
		},
	}
	cmd.Flags().StringVarP(&o.ChosenRig, "rig", "r", "", "Manually pick a rigging to generate Dockerfile")

	return cmd
}

func (o *genOption) getWorkspace() (string, error) {
	workspace := o.Path
	if workspace == "" {
		wd, err := os.Getwd()
		if err != nil {
			return "", err
		}
		workspace = wd
	}
	if _, err := os.Stat(workspace); err != nil {
		return "", err
	}
	return workspace, nil
}

func (o *genOption) Run() error {
	workspace, err := o.getWorkspace()
	if err != nil {
		return err
	}

	var suitableRigging rigging.Rigging
	if o.ChosenRig == "" {
		suitableRiggings := detect(workspace)

		if len(suitableRiggings) == 0 {
			fmt.Println("Failed to detect your application's platform.\nMaybe you can upgrade Derrick to get more platforms supported.")
			return nil
		} else if len(suitableRiggings) > 1 {
			// ask users to choose from one of them
			fmt.Println("More than one rigging can handle the application: %v", printRiggingNames(suitableRiggings))
		}

		suitableRigging = suitableRiggings[0]
	} else {
		suitableRigging = pickRigging(o.ChosenRig)
	}

	templateData, err := suitableRigging.Compile()
	if err != nil {
		return err
	}

	fmt.Printf("Successfully detected your platform is '%s'\n", suitableRigging.Name())
	if err := renderTemplates(suitableRigging, templateData, workspace, o.TemplateFS); err != nil {
		return err
	}

	// write configuration context to a file located in the application folder
	data, err := json.MarshalIndent(templateData, "", "  ")
	if err != nil {
		return err
	}
	if err := ioutil.WriteFile(filepath.Join(workspace, common.DerrickConf), data, 0600); err != nil {
		return err
	}
	fmt.Printf("Successfully generated: %s\n", common.DerrickConf)
	return nil
}

func printRiggingNames(riggings []rigging.Rigging) []string {
	var res []string
	for _, r := range riggings {
		res = append(res, r.Name())
	}
	return res
}

func detect(projectPath string) []rigging.Rigging {
	allRiggings := runtime.GetRiggings()
	if projectPath == "" {
		projectPath = "./"
	}

	var suitableRiggings []rigging.Rigging
	for _, rig := range allRiggings {
		ok := rig.Detect(projectPath)
		if !ok {
			continue
		}
		suitableRiggings = append(suitableRiggings, rig)
	}
	return suitableRiggings
}

func pickRigging(name string) rigging.Rigging {
	allRiggings := runtime.GetRiggings()
	for _, rig := range allRiggings {
		if rig.Name() != name {
			continue
		}
		return rig
	}
	return nil
}

func renderTemplates(rig rigging.Rigging, templateData map[string]string, workspace string, templateFS embed.FS) error {
	templateDir := filepath.Join("static", "rigging", rig.Name(), "templates")

	return fs.WalkDir(templateFS, templateDir, func(templatePath string, entry fs.DirEntry, err error) error {
		if templatePath == templateDir {
			return nil
		}
		// originPath is like "static/.../templates/..."
		path := removeTemplateDirPrefix(templatePath, templateDir)

		if entry.IsDir() {
			return os.MkdirAll(path, 0700)
		}

		if !strings.HasSuffix(entry.Name(), ".tmpl") {
			return copyOriginFile(templateFS, templatePath, path)
		}

		renderedTemplate, err := renderTemplate(templateFS, templatePath, templateData)
		if err != nil {
			return err
		}

		templateBaseName := entry.Name()[0 : len(entry.Name())-len(".tmpl")]
		finalName := filepath.Join(filepath.Dir(path), templateBaseName)
		if err := ioutil.WriteFile(filepath.Join(workspace, finalName), []byte(renderedTemplate), 0600); err != nil {
			return err
		}
		fmt.Printf("Successfully generated: %s\n", finalName)
		return nil
	})
}

func removeTemplateDirPrefix(path string, dir string) string {
	return path[len(dir)+1:]
}

func convertSpecialFiles(path string) string {
	// go embed excludes files whose names begin with "." or "_"
	switch filepath.Base(path) {
	case "helm_helpers":
		return filepath.Join(filepath.Dir(path), "_helpers.tpl")
	case "helm_ignore":
		return filepath.Join(filepath.Dir(path), ".helmignore")
	default:
		return path
	}
}

func copyOriginFile(templateFS embed.FS, path2read, path2write string) error {
	f, err := templateFS.Open(path2read)
	if err != nil {
		return err
	}
	b, err := ioutil.ReadAll(f)
	if err != nil {
		return err
	}
	finalpath := convertSpecialFiles(path2write)
	if err := ioutil.WriteFile(finalpath, b, 0600); err != nil {
		return err
	}
	fmt.Printf("Successfully generated: %s\n", finalpath)
	return nil
}

func renderTemplate(templateFS embed.FS, path string, templateData map[string]string) (string, error) {
	var tctx pkgtemplate.TemplateContext
	if err := mapstructure.Decode(templateData, &tctx); err != nil {
		return "", err
	}
	f, err := templateFS.Open(path)
	if err != nil {
		return "", err
	}
	data, err := ioutil.ReadAll(f)
	if err != nil {
		return "", err
	}

	tmpl, err := template.New(path).Funcs(template.FuncMap(sprig.FuncMap())).Parse(string(data))
	if err != nil {
		return "", err
	}
	var wr bytes.Buffer
	err = tmpl.Execute(&wr, tctx)
	if err != nil {
		return "", err
	}
	return wr.String(), nil
}
