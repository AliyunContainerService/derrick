package java

import (
	"github.com/alibaba/derrick/common"
	"github.com/alibaba/derrick/detectors/general"
	image "github.com/alibaba/derrick/detectors/image/java"
	platform "github.com/alibaba/derrick/detectors/platform/golang"
	"os"
	"path/filepath"
)

type JavaRigging struct {
}

const Platform = "Maven"

func (rig JavaRigging) Detect(workspace string) (bool, string) {
	pom := filepath.Join(workspace, "pom.xml")
	if _, err := os.Stat(pom); err == nil {
		return true, Platform
	}
	return false, ""
}

func (rig JavaRigging) Compile() (map[string]string, error) {
		dr := &common.DetectorReport{
			Nodes: map[string]common.DetectorReport{},
			Store: map[string]string{},
		}
		if err := dr.RegisterDetector(general.ImageRepoDetector{}, common.Meta); err != nil {
			return nil, err
		}
		if err := dr.RegisterDetector(image.JavaVersionDetector{}, common.Dockerfile); err != nil {
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
