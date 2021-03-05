package common

type AutoParam interface {
	Execute() (map[string]string, error)
	Name() string
}
type TemplateRenderContext struct {
	ImageWithTag   string
	Version        string
	ProjectFolder  string
	DerrickVersion string
	ProjectName    string
}

const (
	ImageWithTag   string = "ImageWithTag"
	Version        string = "Version"
	ProjectFolder  string = "ProjectFolder"
	DerrickVersion string = "DerrickVersion"
	ProjectName    string = "ProjectName"
)
