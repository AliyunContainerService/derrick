package template

type TemplateContext struct {
	ImageWithTag    string
	Version         string
	ProjectFolder   string
	DerrickVersion  string
	ProjectName     string
	ArtifactName    string
	JavaToolOptions string
}

const (
	ImageWithTag    string = "ImageWithTag"
	Version         string = "Version"
	ProjectFolder   string = "ProjectFolder"
	DerrickVersion  string = "DerrickVersion"
	ProjectName     string = "ProjectName"
	ArtifactName    string = "ArtifactName"
	JavaToolOptions string = "JavaToolOptions"
)
