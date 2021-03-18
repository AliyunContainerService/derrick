package java

import (
	"os"

	"github.com/alibaba/derrick/pkg/template"
)

type ToolOptionsAutoParam struct {
}

func (detector *ToolOptionsAutoParam) Execute() (map[string]string, error) {
	val := os.Getenv("JAVA_TOOL_OPTIONS")
	if val == "" {
		return nil, nil
	}
	return map[string]string{
		template.JavaToolOptions: val,
	}, nil
}

func (detector *ToolOptionsAutoParam) Name() string {
	return "MvnArtifactAutoParam"
}
