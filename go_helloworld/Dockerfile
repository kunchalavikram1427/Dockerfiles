FROM golang:1.16-alpine
WORKDIR /app
COPY main.go .
RUN go build main.go
CMD [ "/main" ]
