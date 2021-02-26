package php

import (
	"os"
	"path/filepath"

	"github.com/alibaba/derrick/pkg/rigging"
)

type phpRigging struct {
}

func NewRigging() rigging.Rigging {
	return &phpRigging{}
}

func (rig *phpRigging) Name() string {
	return "php"
}
func (rig *phpRigging) Detect(workspace string) bool {
	composer := filepath.Join(workspace, "composer.json")
	if _, err := os.Stat(composer); err == nil {
		return true
	}
	return false
}

func (rig *phpRigging) Compile() (map[string]string, error) {
	return nil, nil
}
