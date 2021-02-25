package common

type Detector interface {
	Execute() (map[string]string, error)
	Name() string
}

const (
	ImageWithTag   string = "ImageWithTag"
	Version        string = "Version"
	ProjectFolder  string = "ProjectFolder"
	DerrickVersion string = "DerrickVersion"
	ProjectName    string = "ProjectName"
)
