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
)

type genOption struct {
	Path       string
	Image      string
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
	cmd.Flags().StringVarP(&o.Path, "path", "p", "", "Path of a project which is about to be detected")
	cmd.Flags().StringVarP(&o.Image, "image", "i", "", "The image and its tag which will be built")
	return cmd
}

func (o *genOption) checkWorkspace() (string, error) {
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
	workspace, err := o.checkWorkspace()
	if err != nil {
		return err
	}

	suitableRiggings := detect(workspace)

	if len(suitableRiggings) == 0 {
		fmt.Println("Failed to detect your application's platform.\nMaybe you can upgrade Derrick to get more platforms supported.")
		return nil
	} else if len(suitableRiggings) > 1 {
		// ask users to choose from one of them
		fmt.Println("More than one rigging can handle the application: %v", printRiggingNames(suitableRiggings))
	}

	suitableRigging := suitableRiggings[0]
	detectedParam, err := suitableRigging.Compile()
	if err != nil {
		return err
	}

	fmt.Printf("Successfully detected your platform is '%s'\n", suitableRigging.Name())
	if err := renderTemplates(suitableRigging, detectedParam, workspace, o.TemplateFS); err != nil {
		return err
	}

	// write configuration context to a file located in the application folder
	data, err := json.Marshal(detectedParam)
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

func renderTemplates(rig rigging.Rigging, detectedParam map[string]string, destDir string, templateFS embed.FS) error {
	templateDir := filepath.Join("static", "rigging", rig.Name(), "templates")
	var templates []string
	err := fs.WalkDir(templateFS, templateDir, func(path string, d fs.DirEntry, err error) error {
		info, err := d.Info()
		if err != nil {
			return err
		}
		if d != nil && strings.HasSuffix(info.Name(), ".tmpl") {
			templates = append(templates, info.Name())
		}
		return nil
	})
	if err != nil {
		return err
	}
	for _, t := range templates {
		renderedTemplate, err := renderTemplate(templateDir, t, detectedParam, templateFS)
		if err != nil {
			return err
		}
		renderedTemplateName := strings.Split(t, ".tmpl")
		if len(renderedTemplateName) != 2 {
			return fmt.Errorf("template %s is not in the right format", t)
		}
		fname := filepath.Join(destDir, renderedTemplateName[0])
		if err := ioutil.WriteFile(fname, []byte(renderedTemplate), 0600); err != nil {
			return err
		}
		fmt.Printf("Successfully generated: %s\n", renderedTemplateName[0])
	}
	return nil
}

func renderTemplate(templateDir, templateFile string, detectedParam map[string]string, templateFS embed.FS) (string, error) {
	var tctx common.TemplateRenderContext
	if err := mapstructure.Decode(detectedParam, &tctx); err != nil {
		return "", err
	}
	f, err := templateFS.Open(filepath.Join(templateDir, templateFile))
	if err != nil {
		return "", err
	}
	data, err := ioutil.ReadAll(f)
	if err != nil {
		return "", err
	}

	tmpl, err := template.New(templateFile).Funcs(template.FuncMap(sprig.FuncMap())).Parse(string(data))
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
