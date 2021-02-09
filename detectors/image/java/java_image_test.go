package java

import (
	"github.com/alibaba/derrick/common"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestExecute(t *testing.T){
	detector := JavaVersionDetector{}
	got, err := detector.Execute()
	assert.NoError(t, err)
	assert.Equal(t, got[common.Version], "13")
}