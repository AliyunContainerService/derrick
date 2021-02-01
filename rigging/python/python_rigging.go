package python

import (
	"os"
	"path/filepath"
)

const Platform string = "Python"

type PythonRigging struct {
}

func (rig PythonRigging) Detect(workspace string) (bool, string) {
	requirementsTxt := filepath.Join(workspace, "requirements.txt")
	setupPy := filepath.Join(workspace, "setup.py")
	if _, err := os.Stat(requirementsTxt); err == nil {
		if _, err := os.Stat(setupPy); err == nil {
			return true, Platform
		}
	}
	return false, ""
}

func (rig PythonRigging) Compile() (map[string]string, error) {
	return nil, nil
}
