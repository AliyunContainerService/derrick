package common

import (
	"encoding/json"
	"io/ioutil"
	"path/filepath"
)

type TemplateRenderContext struct {
	ImageWithTag   string
	Version        string
	ProjectFolder  string
	DerrickVersion string
	ProjectName    string
}

func GetBuildContext(workspace string) (*TemplateRenderContext, error) {
	var ctx TemplateRenderContext
	data, err := ioutil.ReadFile(filepath.Join(workspace, DerrickApplicationConf))
	if err != nil {
		return nil, err
	}
	if err := json.Unmarshal(data, &ctx); err != nil {
		return nil, err
	}
	return &ctx, nil
}
