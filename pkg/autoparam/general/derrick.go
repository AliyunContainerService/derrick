package general

import (
	"path/filepath"

	"github.com/alibaba/derrick/pkg/template"
	"github.com/alibaba/derrick/pkg/version"
)

type DerrickDetector struct {
}

func getProjectName() (string, error) {
	p, err := filepath.Abs(".")
	if err != nil {
		return "", err
	}
	return filepath.Base(p), nil
}

func (detector DerrickDetector) Execute() (map[string]string, error) {
	var projectName = "default"
	base, err := getProjectName()
	if err != nil {
		return nil, err
	}
	if base != "" {
		projectName = base
	}
	return map[string]string{
		template.DerrickVersion: version.Version,
		template.ProjectName:    projectName,
	}, nil

}

func (detector DerrickDetector) Name() string {
	return "DerrickDetector"
}
