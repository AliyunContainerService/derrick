package python

import (
	"os"
	"path/filepath"
)

type PythonRigging struct {
}

func (rig PythonRigging) Name() string {
	return "python"
}
func (rig PythonRigging) Detect(workspace string) bool {
	requirementsTxt := filepath.Join(workspace, "requirements.txt")
	setupPy := filepath.Join(workspace, "setup.py")
	if _, err := os.Stat(requirementsTxt); err == nil {
		if _, err := os.Stat(setupPy); err == nil {
			return true
		}
	}
	return false
}

func (rig PythonRigging) Compile(dockerImage string) (map[string]string, error) {
	return nil, nil
}
