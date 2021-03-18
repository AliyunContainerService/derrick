package golang

import (
	"io"
	"os"
	"path/filepath"
	"strings"

	"github.com/alibaba/derrick/pkg/autoparam"
	"github.com/alibaba/derrick/pkg/autoparam/general"
	image "github.com/alibaba/derrick/pkg/autoparam/image/golang"
	platform "github.com/alibaba/derrick/pkg/autoparam/platform/golang"
	"github.com/alibaba/derrick/pkg/rigging"
)

type golangRigging struct {
}

func NewRigging() rigging.Rigging {
	return &golangRigging{}
}

func (rig *golangRigging) Name() string {
	return "golang"
}

func (rig *golangRigging) Detect(workspace string) bool {
	var detected bool
	err := filepath.Walk(workspace, func(workspace string, info os.FileInfo, err error) error {
		if strings.HasSuffix(info.Name(), ".go") {
			detected = true
			return io.EOF
		}
		return nil
	})
	if err == io.EOF && detected {
		return true
	}
	return false
}

func (rig *golangRigging) Compile() (map[string]string, error) {
	dr := autoparam.NewParamReport()

	if err := dr.AddAutoParam(image.GolangVersionDetector{}); err != nil {
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
