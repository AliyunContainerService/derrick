package runtime

import (
	"github.com/alibaba/derrick/pkg/rigging"
	"github.com/alibaba/derrick/pkg/rigging/golang"
	"github.com/alibaba/derrick/pkg/rigging/java"
	"github.com/alibaba/derrick/pkg/rigging/nodejs"
	"github.com/alibaba/derrick/pkg/rigging/php"
	"github.com/alibaba/derrick/pkg/rigging/python"
)

var storedRiggings []rigging.Rigging

func GetRiggings() []rigging.Rigging {
	return storedRiggings
}

func LoadRiggings() {
	storedRiggings = []rigging.Rigging{
		golang.NewRigging(),
		java.NewRigging(),
		nodejs.NewRigging(),
		php.NewRigging(),
		python.NewRigging(),
	}
}
