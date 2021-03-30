# version
PROJECT_VERSION ?= master
# Repo info
GIT_COMMIT          ?= git-$(shell git rev-parse --short HEAD)
GIT_COMMIT_LONG     ?= $(shell git rev-parse HEAD)
PROJECT_VERSION_VAR    := github.com/alibaba/derrick/pkg/version.Version
PROJECT_GITVERSION_VAR := github.com/alibaba/derrick/pkg/version.GitRevision
LDFLAGS             ?= "-X $(PROJECT_VERSION_VAR)=$(PROJECT_VERSION) -X $(PROJECT_GITVERSION_VAR)=$(GIT_COMMIT)"

GOX         = go run github.com/mitchellh/gox
TARGETS     := darwin/amd64 linux/amd64 windows/amd64
DIST_DIRS   := find * -type d -exec

all: build

build:
	go build -o _bin/derrick main.go

cross-build:
	GO111MODULE=on CGO_ENABLED=0 $(GOX) -ldflags $(LDFLAGS) -parallel=2 -output="_bin/{{.OS}}-{{.Arch}}/derrick" -osarch='$(TARGETS)' main.go

compress:
	( \
		echo "\n## Release Info\nVERSION: $(PROJECT_VERSION)" >> README.md && \
		echo "GIT_COMMIT: $(GIT_COMMIT_LONG)\n" >> README.md && \
		cd _bin && \
		$(DIST_DIRS) cp ../LICENSE {} \; && \
		$(DIST_DIRS) cp ../README.md {} \; && \
		$(DIST_DIRS) tar -zcf derrick-{}.tar.gz {} \; && \
		$(DIST_DIRS) zip -r derrick-{}.zip {} \; && \
		sha256sum derrick-* > sha256sums.txt \
	)