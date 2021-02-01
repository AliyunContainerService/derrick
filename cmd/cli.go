package cmd

import (
	"fmt"
	"runtime"

	"github.com/cloud-native-application/derrick-go/core"
	"github.com/spf13/cobra"
)

// Commands will contain all commands
func Commands() *cobra.Command {
	// ioStream := util.IOStreams{In: os.Stdin, Out: os.Stdout, ErrOut: os.Stderr}

	cmd := &cobra.Command{
		Use:   "derrick-go",
		Short: "🐳 A tool to help you containerize application in seconds",
		Long:  "🐳 A tool to help you containerize application in seconds",
		//Run: func(cmd *cobra.Command, args []string) {
		//
		//	cmd.Println("Flags:")
		//	cmd.Println("  -h, --help   help for derrick")
		//	cmd.Println()
		//	cmd.Println(`Use "derrick [command] --help" for more information about a command.`)
		//},
	}

	cmd.AddCommand(
		NewVersionCommand(),
		Init(),
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
