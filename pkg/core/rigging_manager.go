package core

import (
	"github.com/alibaba/derrick/pkg/common"
	"github.com/alibaba/derrick/pkg/rigging/golang"
	"github.com/alibaba/derrick/pkg/rigging/java"
	"github.com/alibaba/derrick/pkg/rigging/nodejs"
	"github.com/alibaba/derrick/pkg/rigging/php"
	"github.com/alibaba/derrick/pkg/rigging/python"
)

func LoadRiggings() []ExtensionPoint {
	riggings := []common.Rigging{
		golang.GolangRigging{},
		java.JavaRigging{},
		nodejs.NodeJSRigging{},
		php.PHPRigging{},
		python.PythonRigging{},
	}
	extensionPoints := make([]ExtensionPoint, len(riggings))
	for i, rig := range riggings {
		extensionPoints[i] = Register(rig)
	}
	return extensionPoints

	//TODO(zzxwill) Load developer's custom rigging
}
