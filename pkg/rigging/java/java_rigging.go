package java

import (
	"os"
	"path/filepath"

	"github.com/alibaba/derrick/pkg/common"
	"github.com/alibaba/derrick/pkg/detectors/general"
	image "github.com/alibaba/derrick/pkg/detectors/image/java"
)

type JavaRigging struct {
}

func (rig JavaRigging) Name() string {
	return "java"
}
func (rig JavaRigging) Detect(workspace string) bool {
	pom := filepath.Join(workspace, "pom.xml")
	if _, err := os.Stat(pom); err == nil {
		return true
	}
	return false
}

func (rig JavaRigging) Compile(dockerImage string) (map[string]string, error) {
	dr := &common.DetectorReport{
		Nodes: map[string]common.DetectorReport{},
		Store: map[string]string{},
	}
	if err := dr.RegisterDetector(general.ImageRepoDetector{DockerImage: dockerImage}, common.Meta); err != nil {
		return nil, err
	}
	if err := dr.RegisterDetector(image.JavaVersionDetector{}, common.Dockerfile); err != nil {
		return nil, err
	}
	if err := dr.RegisterDetector(general.DerrickDetector{}, common.KubernetesDeployment); err != nil {
		return nil, err
	}
	return dr.GenerateReport(), nil
}
