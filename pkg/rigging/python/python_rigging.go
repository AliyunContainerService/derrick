package python

import (
	"os"
	"path/filepath"

	"github.com/alibaba/derrick/pkg/rigging"
)

type pythonRigging struct {
}

func NewRigging() rigging.Rigging {
	return &pythonRigging{}
}

func (rig *pythonRigging) Name() string {
	return "python"
}
func (rig *pythonRigging) Detect(workspace string) bool {
	requirementsTxt := filepath.Join(workspace, "requirements.txt")
	if _, err := os.Stat(requirementsTxt); err != nil {
		return false
	}

	setupPy := filepath.Join(workspace, "setup.py")
	if _, err := os.Stat(setupPy); err != nil {
		return false
	}

	return true
}

func (rig *pythonRigging) Compile() (map[string]string, error) {
	return nil, nil
}
