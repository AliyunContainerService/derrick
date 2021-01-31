package core

import (
	"github.com/cloud-native-application/derrick-go/common"
	"github.com/cloud-native-application/derrick-go/rigging/golang"
	"github.com/cloud-native-application/derrick-go/rigging/maven"
	"github.com/cloud-native-application/derrick-go/rigging/nodejs"
	"github.com/cloud-native-application/derrick-go/rigging/php"
	"github.com/cloud-native-application/derrick-go/rigging/python"
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
