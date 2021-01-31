package nodejs

import (
	"os"
	"path/filepath"

	"github.com/cloud-native-application/derrick-go/common"
	"github.com/cloud-native-application/derrick-go/detectors/general"
	image "github.com/cloud-native-application/derrick-go/detectors/image/nodejs"
	platform "github.com/cloud-native-application/derrick-go/detectors/platform/golang"
)

const Platform = "NodeJS"

type NodeJSRigging struct {
}

func (rig NodeJSRigging) Detect(workspace string) (bool, string) {
	packageJSON := filepath.Join(workspace, "package.json")
	if _, err := os.Stat(packageJSON); err == nil {
		return true, Platform
	}
	return false, ""
}

func (rig NodeJSRigging) Compile() (map[string]string, error) {
	dr := &common.DetectorReport{
		Nodes: map[string]common.DetectorReport{},
		Store: map[string]string{},
	}
	if err := dr.RegisterDetector(general.ImageRepoDetector{}, common.Meta); err != nil {
		return nil, err
	}
	if err := dr.RegisterDetector(image.NodeJSVersionDetector{}, common.Dockerfile); err != nil {
		return nil, err
	}
	if err := dr.RegisterDetector(platform.PackageNameDetector{}, common.Dockerfile); err != nil {
		return nil, err
	}
	if err := dr.RegisterDetector(general.DerrickDetector{}, common.KubernetesDeployment); err != nil {
		return nil, err
	}
	return dr.GenerateReport(), nil
}
