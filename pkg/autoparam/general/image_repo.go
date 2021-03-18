package general

import (
	"fmt"

	"github.com/AlecAivazis/survey/v2"

	"github.com/alibaba/derrick/pkg/template"
)

type ImageRepoDetector struct {
	DockerImage string
}

func (detector ImageRepoDetector) Execute() (map[string]string, error) {
	image := detector.DockerImage
	if image == "" {
		prompt := &survey.Input{
			Message: "Please input image name with tag (such as \"registry.com/user/repo:tag\"): ",
		}
		err := survey.AskOne(prompt, &image, survey.WithValidator(survey.Required))
		if err != nil {
			return nil, fmt.Errorf("hit an issue to fetch image name: %w", err)
		}
	}
	result := map[string]string{
		template.ImageWithTag: image,
	}
	return result, nil
}

func (detector ImageRepoDetector) Name() string {
	return "ImageRepoDetector"
}
