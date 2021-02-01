package nodejs

import "github.com/cloud-native-application/derrick-go/common"

const DefaultVersion = "3.12"

type NodeJSVersionDetector struct {
}

func (detector NodeJSVersionDetector) Execute() (map[string]string, error) {
	return map[string]string{common.Version: DefaultVersion}, nil
}

func (detector NodeJSVersionDetector) Name() string {
	return "GolangVersionDetector"
}
