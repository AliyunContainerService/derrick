package engine

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os/exec"
	"path/filepath"

	"github.com/alibaba/derrick/pkg/common"
	"github.com/alibaba/derrick/pkg/template"
)

func BuildImage(workspace string) error {
	buildContext, err := GetBuildContext(workspace)
	if err != nil {
		return err
	}
	dockerImage := buildContext.ImageWithTag
	if dockerImage == "" {
		return fmt.Errorf("could not find the imaage you set before, please run `derrick gen` again")
	}
	cmd := exec.Command("bash", "-c", fmt.Sprintf("docker build -t %s .", dockerImage))
	if err := common.RealtimePrintCommandOutput(cmd, ""); err != nil {
		// TODO(zzxwill) need to check whether Docker is installed
		return err
	}
	fmt.Println(fmt.Sprintf("The application image %s has been successfully built.", dockerImage))
	return nil
}

func DeployToKubernetes(workspace string) error {
	buildContext, err := GetBuildContext(workspace)
	if err != nil {
		return err
	}
	dockerImage := buildContext.ImageWithTag
	if dockerImage == "" {
		return fmt.Errorf("could not find the imaage you set before, please run `derrick gen` again")
	}

	cmd := exec.Command("bash", "-c", fmt.Sprintf("docker push %s", buildContext.ImageWithTag))
	if err := common.RealtimePrintCommandOutput(cmd, ""); err != nil {
		return err
	}
	cmd = exec.Command("bash", "-c", fmt.Sprintf("kubectl apply -f %s", common.KubernetesDeployment))
	if err := common.RealtimePrintCommandOutput(cmd, ""); err != nil {
		// TODO(zzxwill) need to check whether `kubectl` isinstalled
		return err
	}
	fmt.Println("Your application has been built and deployed to your Kubernetes cluster! You can run `kubectl get svc` to get exposed ports.")
	return nil
}

func GetBuildContext(workspace string) (*template.TemplateContext, error) {
	var ctx template.TemplateContext
	data, err := ioutil.ReadFile(filepath.Join(workspace, common.DerrickConf))
	if err != nil {
		return nil, err
	}
	if err := json.Unmarshal(data, &ctx); err != nil {
		return nil, err
	}
	return &ctx, nil
}
