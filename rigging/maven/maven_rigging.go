package maven

import (
	"os"
	"path/filepath"
)

type MavenRigging struct {
}

const Platform = "Maven"

func (rig MavenRigging) Detect(workspace string) (bool, string) {
	pom := filepath.Join(workspace, "pom.xml")
	if _, err := os.Stat(pom); err == nil {
		return true, Platform
	}
	return false, ""
}

func (rig MavenRigging) Compile() (map[string]string, error) {
	return nil, nil
}
