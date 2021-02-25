package common

import (
	"fmt"
	"io"
	"os"
	"os/exec"
	"path/filepath"
)

const (
	DerrickHome    = ".derrick"
	DerrickHomeEnv = "DERRICK_HOME"
	DerrickLogo    = `
8888888b.                       d8b        888
888  "Y88b                      Y8P        888
888    888                                 888
888    888 .d88b. 888d888888d888888 .d8888b888  888
888    888d8P  Y8b888P"  888P"  888d88P"   888 .88P
888    88888888888888    888    888888     888888K
888  .d88PY8b.    888    888    888Y88b.   888 "88b
8888888P"  "Y8888 888    888    888 "Y8888P888  888

===================================================
Derrick is a scaffold tool to migrate applications
You can use Derrick to migrate your project simply.
===================================================
`
	DERRICK_VERSION        = "0.0.1"
	DerrickApplicationConf = "derrick_conf"
)

const (
	Meta                 = "Meta"
	Dockerfile           = "Dockerfile"
	DockerCompose        = "DockerCompose"
	KubernetesDeployment = "kubernetes-deployment.yaml"
)

// GetDerrickHome return vela home dir
func GetDerrickHome() (string, error) {
	if custom := os.Getenv(DerrickHomeEnv); custom != "" {
		return custom, nil
	}
	home, err := os.UserHomeDir()
	if err != nil {
		return "", err
	}
	return filepath.Join(home, DerrickHome), nil
}

// CheckDerrickFirstSetup checks if derrick is used for the first time
func CheckDerrickFirstSetup() (bool, error) {
	derrickHome, err := GetDerrickHome()
	if err != nil {
		return true, fmt.Errorf("failed to get Derrick home, err: %s", err)
	}

	riggingHome, err := GetRiggingHome()
	if err != nil {
		return true, fmt.Errorf("failed to get Rigging home, err: %s", err)
	}

	commandsHome, err := GetCommandsHome()
	if err != nil {
		return true, fmt.Errorf("failed to get CommandsHome home, err: %s", err)
	}

	if _, err := os.Stat(derrickHome); err != nil {
		return true, err
	}
	if _, err := os.Stat(riggingHome); err != nil {
		return true, err
	}
	if _, err := os.Stat(commandsHome); err != nil {
		return true, err
	}

	return false, nil
}

func GetRiggingHome() (string, error) {
	home, err := GetDerrickHome()
	if err != nil {
		return "", err
	}
	return filepath.Join(home, "rigging"), nil
}

func GetCommandsHome() (string, error) {
	home, err := GetDerrickHome()
	if err != nil {
		return "", err
	}
	return filepath.Join(home, "commands"), nil
}

// InitDirs create dir if not exits
func InitDirs() error {
	if err := InitDerrickDir(); err != nil {
		return err
	}
	if err := InitRiggingDir(); err != nil {
		return err
	}
	if err := InitCommandsDir(); err != nil {
		return err
	}
	return nil
}

func InitDerrickDir() error {
	home, err := GetDerrickHome()
	if err != nil {
		return err
	}
	return os.MkdirAll(home, 0755)
}

func InitRiggingDir() error {
	home, err := GetRiggingHome()
	if err != nil {
		return err
	}
	return os.MkdirAll(home, 0755)
}

func InitCommandsDir() error {
	home, err := GetCommandsHome()
	if err != nil {
		return err
	}
	return os.MkdirAll(home, 0755)
}

func CheckDerrickInitStep(workspace string) bool {
	if _, err := os.Stat(filepath.Join(workspace, DerrickApplicationConf)); err == nil {
		return true
	}
	return false
}

func CheckDockerFileExisted(workspace string) bool {
	if _, err := os.Stat(filepath.Join(workspace, Dockerfile)); err == nil {
		return true
	}
	return false
}

// RealtimePrintCommandOutput prints command output in real time
// If logFile is "", it will prints the stdout, or it will write to local file
func RealtimePrintCommandOutput(cmd *exec.Cmd, logFile string) error {
	var writer io.Writer
	if logFile == "" {
		writer = io.MultiWriter(os.Stdout)
	} else {
		if _, err := os.Stat(filepath.Dir(logFile)); err != nil {
			return err
		}
		f, err := os.Create(filepath.Clean(logFile))
		if err != nil {
			return err
		}
		writer = io.MultiWriter(f)
	}
	cmd.Stdout = writer
	cmd.Stderr = writer
	if err := cmd.Run(); err != nil {
		return err
	}
	return nil
}
