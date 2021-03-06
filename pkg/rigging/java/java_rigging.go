package java

import (
	"os"
	"path/filepath"

	"github.com/alibaba/derrick/pkg/common"
	"github.com/alibaba/derrick/pkg/detectors/general"
	"github.com/alibaba/derrick/pkg/rigging"
)

type javaRigging struct {
}

func NewRigging() rigging.Rigging {
	return &javaRigging{}
}

func (rig *javaRigging) Name() string {
	return "java"
}
func (rig *javaRigging) Detect(workspace string) bool {
	pom := filepath.Join(workspace, "pom.xml")
	if _, err := os.Stat(pom); err == nil {
		return true
	}
	return false
}

func (rig *javaRigging) Compile() (map[string]string, error) {
	dr := &common.ParamReport{
		Store: map[string]string{},
	}
	if err := dr.RegisterAutoParam(general.DerrickDetector{}); err != nil {
		return nil, err
	}
	return dr.GenerateReport(), nil
}
