package autoparam

type AutoParam interface {
	Execute() (map[string]string, error)
	Name() string
}
