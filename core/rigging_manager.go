package core

import (
	"github.com/alibaba/derrick/common"
	"github.com/alibaba/derrick/rigging/golang"
	"github.com/alibaba/derrick/rigging/maven"
	"github.com/alibaba/derrick/rigging/nodejs"
	"github.com/alibaba/derrick/rigging/php"
	"github.com/alibaba/derrick/rigging/python"
)

//type Rigging interface {
//	GetTemplateDir() string
//	GetTemplateName() string
//}

//func GetTemplateDir(platform interface{}) string {
//	return reflect.TypeOf(platform).PkgPath()
//}
//
//func GetTemplateName(platform interface{}) interface{} {
//	return reflect.TypeOf(platform).Name()
//}

func LoadRiggings() []ExtensionPoint {
	riggings := []common.Rigging{golang.GolangRigging{}, maven.MavenRigging{}, nodejs.NodeJSRigging{}, php.PHPRigging{}, python.PythonRigging{}}
	extensionPoints := make([]ExtensionPoint, len(riggings))
	for i, rig := range riggings {
		extensionPoints[i] = Register(rig)
	}
	return extensionPoints

	//TODO(zzxwill) Load developer's custom rigging
}
