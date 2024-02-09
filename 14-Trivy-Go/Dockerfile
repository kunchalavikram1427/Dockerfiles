FROM golang:1.16-alpine as BUILD
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o /bin/hello
ENV secret=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
EXPOSE 8080
CMD [ "/bin/hello" ]