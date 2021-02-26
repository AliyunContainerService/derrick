package php

import (
	"os"
	"path/filepath"
)

type PHPRigging struct {
}

func (rig PHPRigging) Name() string {
	return "php"
}
func (rig PHPRigging) Detect(workspace string) bool {
	composer := filepath.Join(workspace, "composer.json")
	if _, err := os.Stat(composer); err == nil {
		return true
	}
	return false
}

func (rig PHPRigging) Compile(dockerImage string) (map[string]string, error) {
	return nil, nil
}
