package general

import (
	"encoding/xml"
	"fmt"
	"io/ioutil"

	"github.com/creekorful/mvnparser"

	"github.com/alibaba/derrick/pkg/template"
)

type MvnArtifactAutoParam struct {
}

func (detector *MvnArtifactAutoParam) Execute() (map[string]string, error) {
	pomStr, err := ioutil.ReadFile("pom.xml")
	if err != nil {
		return nil, err
	}

	var project mvnparser.MavenProject
	if err := xml.Unmarshal(pomStr, &project); err != nil {
		return nil, fmt.Errorf("unable to unmarshal pom file. Reason: %s", err)
	}

	return map[string]string{
		template.ArtifactName: fmt.Sprintf("%s-%s", project.ArtifactId, project.Version),
	}, nil
}

func (detector *MvnArtifactAutoParam) Name() string {
	return "MvnArtifactAutoParam"
}
