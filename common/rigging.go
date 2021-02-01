package common

type Rigging interface {
	Detect(workspace string) (bool, string)
	Compile() (map[string]string, error)
}
