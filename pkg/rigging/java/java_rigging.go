package java

import (
	"os"
	"path/filepath"

	"github.com/alibaba/derrick/pkg/autoparam"
	"github.com/alibaba/derrick/pkg/autoparam/general"
	"github.com/alibaba/derrick/pkg/autoparam/java"
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
	dr := autoparam.NewParamReport()
	if err := dr.AddAutoParam(&java.ToolOptionsAutoParam{}); err != nil {
		return nil, err
	}
	if err := dr.AddAutoParam(&java.MvnArtifactAutoParam{}); err != nil {
		return nil, err
	}
	if err := dr.AddAutoParam(general.DerrickDetector{}); err != nil {
		return nil, err
	}
	return dr.TemplateData(), nil
}
