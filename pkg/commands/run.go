package commands

import (
	"embed"
	"fmt"
	"runtime"

	"github.com/spf13/cobra"

	"github.com/alibaba/derrick/pkg/version"
)

// New will contain all commands
func Run(templateFS embed.FS) error {
	// ioStream := util.IOStreams{In: os.Stdin, Out: os.Stdout, ErrOut: os.Stderr}

	cmd := &cobra.Command{
		Use:   "derrick",
		Short: "🐳 A tool to help you containerize applications in seconds",
		Long:  "🐳 A tool to help you containerize applications in seconds",
	}

	cmd.AddCommand(
		NewVersionCommand(),
		NewListCommand(),
		NewGenCommand(templateFS),
		Up(),
	)
	return cmd.Execute()
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
				version.Version,
				version.GitRevision,
				runtime.Version())
		},
	}
}
