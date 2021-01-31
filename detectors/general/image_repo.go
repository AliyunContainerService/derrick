package general

import (
	"fmt"

	"github.com/AlecAivazis/survey/v2"
	"github.com/cloud-native-application/derrick-go/common"
)

type ImageRepoDetector struct {
}

func (detector ImageRepoDetector) Execute() (map[string]string, error) {
	var image string
	prompt := &survey.Input{
		Message: "Please input image name with tag (such as \"registry.com/user/repo:tag\"): ",
	}
	err := survey.AskOne(prompt, &image, survey.WithValidator(survey.Required))
	if err != nil {
		return nil, fmt.Errorf("hit an issue to fetch image name: %w", err)
	}
	result := map[string]string{
		common.ImageWithTag: image,
	}
	return result, nil
}

func (detector ImageRepoDetector) Name() string {
	return "ImageRepoDetector"
}
