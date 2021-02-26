package nodejs

import (
	"os"
	"path/filepath"

	"github.com/alibaba/derrick/pkg/common"
	"github.com/alibaba/derrick/pkg/detectors/general"
	image "github.com/alibaba/derrick/pkg/detectors/image/nodejs"
	platform "github.com/alibaba/derrick/pkg/detectors/platform/golang"
)

type NodeJSRigging struct {
}

func (rig NodeJSRigging) Name() string {
	return "nodejs"
}

func (rig NodeJSRigging) Detect(workspace string) bool {
	packageJSON := filepath.Join(workspace, "package.json")
	if _, err := os.Stat(packageJSON); err == nil {
		return true
	}
	return false
}

func (rig NodeJSRigging) Compile(dockerImage string) (map[string]string, error) {
	dr := &common.DetectorReport{
		Nodes: map[string]common.DetectorReport{},
		Store: map[string]string{},
	}
	if err := dr.RegisterDetector(general.ImageRepoDetector{DockerImage: dockerImage}, common.Meta); err != nil {
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
