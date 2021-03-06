package java

import (
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/alibaba/derrick/pkg/template"
)

func TestExecute(t *testing.T) {
	detector := JavaVersionDetector{}
	got, err := detector.Execute()
	assert.NoError(t, err)
	assert.Equal(t, got[template.Version], "13")
}
