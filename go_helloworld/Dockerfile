FROM golang:1.16-alpine as build
WORKDIR /app
COPY main.go .
RUN go build main.go

FROM alpine:latest
WORKDIR /app
COPY --from=build /app/main .
ENTRYPOINT ["/app/main"]