all: build

build: embed-templates
	go build -o /usr/local/bin/derrick *.go
	rm -f pkged.go


embed-templates:
	go get github.com/markbates/pkger/cmd/pkger
	$(GOPATH)/bin/pkger -include /rigging