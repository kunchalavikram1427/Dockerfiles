FROM golang:1.16-alpine as BUILD
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o /bin/hello

FROM scratch
WORKDIR /
COPY --from=BUILD /bin/hello /bin/hello
EXPOSE 8080
CMD [ "/bin/hello" ]