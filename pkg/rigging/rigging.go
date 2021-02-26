package rigging

type Rigging interface {
	Name() string

	// returns true if it matches, false if not.
	Detect(workspace string) bool

	Compile() (map[string]string, error)
}
