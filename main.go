package main

import (
	"embed"
	"github.com/alibaba/derrick/cmd"
)

//go:embed rigging
var templateFS embed.FS

func main() {
	cmd.Run(templateFS)
}
