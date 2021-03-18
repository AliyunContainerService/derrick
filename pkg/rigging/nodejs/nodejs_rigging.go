package nodejs

import (
	"os"
	"path/filepath"

	"github.com/alibaba/derrick/pkg/autoparam"
	"github.com/alibaba/derrick/pkg/autoparam/general"
	image "github.com/alibaba/derrick/pkg/autoparam/image/nodejs"
	platform "github.com/alibaba/derrick/pkg/autoparam/platform/golang"
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
	dr := autoparam.NewParamReport()
	if err := dr.AddAutoParam(image.NodeJSVersionDetector{}); err != nil {
		return nil, err
	}
	if err := dr.AddAutoParam(platform.PackageNameDetector{}); err != nil {
		return nil, err
	}
	if err := dr.AddAutoParam(general.DerrickDetector{}); err != nil {
		return nil, err
	}
	return dr.TemplateData(), nil
}
