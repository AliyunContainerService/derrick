all: build

build: embed-templates
	go build -o /usr/local/bin/derrick-go *.go
	rm -f pkged.go


embed-templates:
	go get github.com/markbates/pkger/cmd/pkger
	pkger -include /rigging