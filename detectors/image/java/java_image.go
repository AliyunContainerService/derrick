package java

import (
	"os/exec"
	"regexp"
	"strings"

	"github.com/alibaba/derrick/common"
)

const (
	DefaultVersion = "8"
)

type JavaVersionDetector struct {
}

func (detector JavaVersionDetector) Execute() (map[string]string, error) {
	cmd := exec.Command("bash", "-c", "java --version")
	output, err := cmd.Output()
	if err != nil {
		return nil, err
	}
	re, err := regexp.Compile("java [[:digit:]]*.[[:digit:]]*.[[:digit:]]*")
	if err != nil {
		return nil, err
	}
	matched := re.Find(output)
	version := common.Version
	if matched == nil {
		return map[string]string{version: DefaultVersion}, nil
	}
	majorVersion := strings.Split(strings.ReplaceAll(string(matched), "java ", ""), ".")[0]
	return map[string]string{version: majorVersion}, nil
}

func (detector JavaVersionDetector) Name() string {
	return "JavaVersionDetector"
}
