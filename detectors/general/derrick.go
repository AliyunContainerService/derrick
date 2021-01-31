package general

import (
	"path/filepath"

	"github.com/cloud-native-application/derrick-go/common"
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
		common.DerrickVersion: common.DERRICK_VERSION,
		common.ProjectName:    projectName,
	}, nil

}

func (detector DerrickDetector) Name() string {
	return "DerrickDetector"
}
