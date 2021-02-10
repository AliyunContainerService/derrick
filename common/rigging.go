package common

type Rigging interface {
	Detect(workspace string) (bool, string)
	Compile(dockerImage string) (map[string]string, error)
}
