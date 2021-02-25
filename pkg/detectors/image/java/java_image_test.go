package java

import (
	"testing"

	"github.com/stretchr/testify/assert"

	"github.com/alibaba/derrick/pkg/common"
)

func TestExecute(t *testing.T) {
	detector := JavaVersionDetector{}
	got, err := detector.Execute()
	assert.NoError(t, err)
	assert.Equal(t, got[common.Version], "13")
}
