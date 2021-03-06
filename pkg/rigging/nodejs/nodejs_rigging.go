package nodejs

import (
	"os"
	"path/filepath"

	"github.com/alibaba/derrick/pkg/detectors"
	"github.com/alibaba/derrick/pkg/detectors/general"
	image "github.com/alibaba/derrick/pkg/detectors/image/nodejs"
	platform "github.com/alibaba/derrick/pkg/detectors/platform/golang"
	"github.com/alibaba/derrick/pkg/rigging"
)

type nodeJSRigging struct {
}

func NewRigging() rigging.Rigging {
	return &nodeJSRigging{}
}

func (rig *nodeJSRigging) Name() string {
	return "nodejs"
}

func (rig *nodeJSRigging) Detect(workspace string) bool {
	packageJSON := filepath.Join(workspace, "package.json")
	if _, err := os.Stat(packageJSON); err == nil {
		return true
	}
	return false
}

func (rig *nodeJSRigging) Compile() (map[string]string, error) {
	dr := &detectors.ParamReport{
		Store: map[string]string{},
	}
	if err := dr.RegisterAutoParam(image.NodeJSVersionDetector{}); err != nil {
		return nil, err
	}
	if err := dr.RegisterAutoParam(platform.PackageNameDetector{}); err != nil {
		return nil, err
	}
	if err := dr.RegisterAutoParam(general.DerrickDetector{}); err != nil {
		return nil, err
	}
	return dr.GenerateReport(), nil
}
