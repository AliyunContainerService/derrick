package core

import (
	"reflect"

	"github.com/cloud-native-application/derrick-go/common"
)

type ExtensionPoint struct {
	Rigging common.Rigging
}

func getRiggingName(platform interface{}) string {
	return reflect.TypeOf(platform).Name()
}

func loadRigging(detect interface{}) reflect.Value {
	return reflect.ValueOf(detect)
}

func Register(rig common.Rigging) ExtensionPoint {
	return ExtensionPoint{
		Rigging: rig,
	}
}
