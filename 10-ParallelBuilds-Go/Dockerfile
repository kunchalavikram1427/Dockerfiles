# syntax=docker/dockerfile:1
FROM golang:1.20-alpine as base
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .

FROM base as build_client
RUN go build -o /bin/client ./cmd/client

FROM base as build_server
RUN go build -o /bin/server ./cmd/server

FROM scratch as client
COPY --from=build_client /bin/client /bin/
ENTRYPOINT [ "/bin/client" ]

FROM scratch as server
COPY --from=build_server /bin/server /bin/
ENTRYPOINT [ "/bin/server" ]