package golang

import (
	"io"
	"os"
	"path/filepath"
	"strings"

	"github.com/alibaba/derrick/pkg/common"
	"github.com/alibaba/derrick/pkg/detectors/general"
	image "github.com/alibaba/derrick/pkg/detectors/image/golang"
	platform "github.com/alibaba/derrick/pkg/detectors/platform/golang"
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
	dr := &common.ParamReport{
		Nodes: map[string]common.ParamReport{},
		Store: map[string]string{},
	}

	if err := dr.RegisterAutoParam(image.GolangVersionDetector{}, common.Dockerfile); err != nil {
		return nil, err
	}
	if err := dr.RegisterAutoParam(platform.PackageNameDetector{}, common.Dockerfile); err != nil {
		return nil, err
	}

	if err := dr.RegisterAutoParam(general.DerrickDetector{}, common.KubernetesDeployment); err != nil {
		return nil, err
	}
	return dr.GenerateReport(), nil
}
