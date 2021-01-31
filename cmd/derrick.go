package cmd

import (
	"fmt"
	"os"

	"github.com/cloud-native-application/derrick-go/common"
	"github.com/cloud-native-application/derrick-go/core"
)

func Run() {
	if err := load(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	command := Commands()
	if err := command.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

func preLoad() error {
	fmt.Print(common.DerrickLogo)
	if err := common.InitDirs(); err != nil {
		return fmt.Errorf("failed to init Derrick home, err: %s", err)
	}
	return nil
}

func load() error {
	firstTimeFlag, _ := common.CheckDerrickFirstSetup()
	if firstTimeFlag {
		if err := preLoad(); err != nil {
			return err
		}
	}

	core.LoadRiggings()
	return nil
}
