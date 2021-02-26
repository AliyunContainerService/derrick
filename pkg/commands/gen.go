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
	"reflect"
	"strings"
	"text/template"

	"github.com/Masterminds/sprig/v3"
	"github.com/mitchellh/mapstructure"
	"github.com/spf13/cobra"

	"github.com/alibaba/derrick/pkg/common"
	"github.com/alibaba/derrick/pkg/rigging"
)

var projectPath, dockerImage string

func NewGenCommand(templateFS embed.FS) *cobra.Command {
	cmd := &cobra.Command{
		Use:     "gen",
		Short:   "Inspect the application and generate Dockerfile",
		Example: `derrick gen`,
		RunE: func(cmd *cobra.Command, args []string) error {
			return execute(projectPath, dockerImage, templateFS)
		},
	}
	cmd.Flags().StringVarP(&projectPath, "path", "p", "", "Path of a project which is about to be detected")
	cmd.Flags().StringVarP(&dockerImage, "image", "i", "", "The image and its tag which will be built")
	return cmd
}

type SuitableRiggings struct {
	Platform string
	Rigging  rigging.Rigging
}

func execute(workspace, dockerImage string, templateFS embed.FS) error {
	var err error
	if workspace == "" {
		workspace, err = os.Getwd()
		if err != nil {
			return err
		}
	}
	if _, err := os.Stat(workspace); err != nil {
		return err
	}
	suitableRiggings := detect(workspace)
	riggingNo := len(suitableRiggings)
	if riggingNo == 0 {
		fmt.Println("Failed to detect your application's platform.\nMaybe you can upgrade Derrick to get more platforms supported.")
		return nil
	} else if riggingNo > 1 {
		// TODO(zzxwill) ask users to choose from one of them
		fmt.Println("More than one rigging can handle the application.")
		return nil
	}

	suitableRigging := suitableRiggings[0]
	rig := suitableRigging.Rigging
	detectedContext, err := rig.Compile(dockerImage)
	if err != nil {
		return err
	}
	if err := renderTemplates(rig, detectedContext, workspace, templateFS); err != nil {
		return err
	}
	fmt.Printf("Successfully detected your platform is %s and compiled it successfully.\n", suitableRigging.Platform)

	// write configuration context to a file located in the application folder
	data, err := json.Marshal(detectedContext)
	if err != nil {
		return err
	}
	if err := ioutil.WriteFile(filepath.Join(workspace, common.DerrickApplicationConf), data, 0500); err != nil {
		return err
	}
	return nil
}

func detect(projectPath string) []*SuitableRiggings {
	allRigging := rigging.GetAll()
	if projectPath == "" {
		projectPath = "./"
	}
	var suitableRiggings []*SuitableRiggings
	for _, rig := range allRigging {
		success := rig.Detect(projectPath)
		if success {
			suitableRiggings = append(suitableRiggings,
				&SuitableRiggings{
					Platform: rig.Name(),
					Rigging:  rig,
				})
		}
	}
	return suitableRiggings
}

func renderTemplates(rig rigging.Rigging, detectedContext map[string]string, destDir string, templateFS embed.FS) error {
	// TODO(zzxwill) PkgPath() returns something like: github.com/alibaba/derrick/pkg/rigging/golang
	// Need to convert it to something like: static/rigging/golang/templates
	pkgPath := strings.Join(strings.Split(reflect.TypeOf(rig).PkgPath(), "/")[4:], "/")
	templateDir := filepath.Join("static", pkgPath, "templates")
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
		renderedTemplate, err := renderTemplate(templateDir, t, detectedContext, templateFS)
		if err != nil {
			return err
		}
		renderedTemplateName := strings.Split(t, ".tmpl")
		if len(renderedTemplateName) != 2 {
			return fmt.Errorf("template %s is not in the right format", t)
		}
		if err := ioutil.WriteFile(filepath.Join(destDir, renderedTemplateName[0]), []byte(renderedTemplate), 0500); err != nil {
			return err
		}
	}
	return nil
}

func renderTemplate(templateDir, templateFile string, detectedContext map[string]string, templateFS embed.FS) (string, error) {
	var ctx common.TemplateRenderContext
	if err := mapstructure.Decode(detectedContext, &ctx); err != nil {
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
	err = tmpl.Execute(&wr, ctx)
	if err != nil {
		return "", err
	}
	return wr.String(), nil
}
