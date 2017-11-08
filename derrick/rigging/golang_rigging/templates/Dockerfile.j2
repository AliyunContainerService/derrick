# build stage
FROM golang:{{ version }}-alpine3.6 AS build-env
ADD . /src/{{ project_folder }}
ENV GOPATH /:/src/{{ project_folder }}/vendor
WORKDIR /src/{{ project_folder }}
RUN go build -o app


# test stage
#FROM golang:{{ version }}-alpine3.6
#WORKDIR /src/{{ project_folder }}
#RUN go test


# release stage
FROM alpine
WORKDIR /app
EXPOSE 8080
COPY --from=build-env /src/{{ project_folder }}/app /app/
CMD ["./app"]