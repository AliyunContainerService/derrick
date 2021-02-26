package rigging

import (
	"github.com/alibaba/derrick/pkg/rigging/golang"
	"github.com/alibaba/derrick/pkg/rigging/java"
	"github.com/alibaba/derrick/pkg/rigging/nodejs"
	"github.com/alibaba/derrick/pkg/rigging/php"
	"github.com/alibaba/derrick/pkg/rigging/python"
)

var storedRiggings []Rigging

func GetAll() []Rigging {
	return storedRiggings
}

func Load() {
	storedRiggings = []Rigging{
		golang.GolangRigging{},
		java.JavaRigging{},
		nodejs.NodeJSRigging{},
		php.PHPRigging{},
		python.PythonRigging{},
	}
}

type Rigging interface {
	Name() string

	// returns true if it matches, false if not.
	Detect(workspace string) bool

	Compile(dockerImage string) (map[string]string, error)
}
