package commands

import (
	"fmt"
	"os"

	"github.com/alibaba/derrick/pkg/engine"

	"github.com/spf13/cobra"

	"github.com/alibaba/derrick/pkg/common"
)

var workspace string
var deployToKubernetes bool

func Up() *cobra.Command {
	cmd := &cobra.Command{
		Hidden:  true,
		Use:     "up",
		Short:   "Build an image for your application",
		Long:    "Build an image for your application",
		Example: `derrick up`,
		RunE: func(cmd *cobra.Command, args []string) error {
			return build(workspace)
		},
	}
	cmd.Flags().StringVarP(&workspace, "project-path", "p", "", "Path of a project")
	cmd.Flags().BoolVarP(&deployToKubernetes, "deploy-to-kubernetes", "k", false, "Push image and deploy the application to your Kubernetes cluster")
	return cmd
}

func build(workspace string) error {
	if !common.CheckDerrickInitStep(workspace) {
		fmt.Println("Your application hasn't been initialized, please run `derrick gen` first.")
		os.Exit(1)
	}
	if !common.CheckDockerFileExisted(workspace) {
		fmt.Println("Dockerfile doesn't exist. Please rerun `derrick gen`.")
	}
	if err := engine.BuildImage(workspace); err != nil {
		return err
	}
	if deployToKubernetes {
		return engine.DeployToKubernetes(workspace)
	}
	return nil
}
