package platform

import (
	"fmt"
	"os"
	"regexp"
	"strings"

	"github.com/cloud-native-application/derrick-go/common"
)

const SrcTag = "/src/"

type PackageNameDetector struct {
}

func (detector PackageNameDetector) Execute() (map[string]string, error) {
	cwd, err := os.Getwd()
	if err != nil {
		return nil, err
	}
	re, err := regexp.Compile(fmt.Sprintf("%s.*", SrcTag))
	if err != nil {
		return nil, err
	}
	result := re.FindAllString(cwd, -1)
	if len(result) == 0 {
		return nil, fmt.Errorf("the source code is not in GOPATH")
	}
	return map[string]string{common.ProjectFolder: strings.ReplaceAll(result[0], SrcTag, "")}, nil
}

func (detector PackageNameDetector) Name() string {
	return "PackageNameDetector"
}
