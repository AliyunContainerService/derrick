package cmd

import (
	"embed"
	"fmt"
	"runtime"

	"github.com/spf13/cobra"

	"github.com/alibaba/derrick/core"
)

// Commands will contain all commands
func Commands(templateFS embed.FS) *cobra.Command {
	// ioStream := util.IOStreams{In: os.Stdin, Out: os.Stdout, ErrOut: os.Stderr}

	cmd := &cobra.Command{
		Use:   "derrick",
		Short: "🐳 A tool to help you containerize application in seconds",
		Long:  "🐳 A tool to help you containerize application in seconds",
	}

	cmd.AddCommand(
		NewVersionCommand(),
		Init(templateFS),
		Up(),
	)
	return cmd
}

// NewVersionCommand print client version
func NewVersionCommand() *cobra.Command {
	return &cobra.Command{
		Use:   "version",
		Short: "Prints out build version information",
		Long:  "Prints out build version information",
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Printf(`Version: %v
GitRevision: %v
GolangVersion: %v
`,
				core.Version,
				core.GitRevision,
				runtime.Version())
		},
	}
}
