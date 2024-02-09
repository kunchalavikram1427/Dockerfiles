# docker-gs-ping

A simple Go server/microservice example for [Docker's Go Language Guide](https://docs.docker.com/language/golang/).

Notable features:

* https://golangbyexample.com/go-mod-sum-module/
* Includes a [multi-stage `Dockerfile`](https://github.com/olliefr/docker-gs-ping/blob/main/Dockerfile.multistage), which actually is a good example of how to build Go binaries _for production releases_.
* Has functional tests for application's business requirements with proper isolation between tests using [`ory/dockertest`](https://github.com/ory/dockertest).
* Has a CI pipeline using GitHub Actions to run functional tests in independent containers.
* Has a CD pipeline using GitHub Actions to publish to Docker Hub.

Planned:

* Building Go modules and Docker images with `goreleaser`

## Want _moar_?!

There is a more advanced example in [olliefr/docker-gs-ping-roach](https://github.com/olliefr/docker-gs-ping-roach) using [CockroachDB](https://github.com/cockroachdb/cockroach).

## Contributing

This was written for an _introduction_ section of the Docker tutorial and as such it favours brevity and pedagogical clarity over robustness. 

Thus, feedback is welcome, but please no nits or pedantry. Ain't nobody got time for that 🙃



## Trivy scan

trivy image python:3.4-alpine
trivy image gcr.io/distroless/python3-debian12

trivy image --severity CRITICAL golang:1.16-buster
trivy image --severity CRITICAL gcr.io/distroless/base-debian12
trivy image --severity HIGH,CRITICAL ruby:2.4.0

trivy image kunchalavikram/trivy-test:v1
trivy image kunchalavikram/trivy-test:v2

trivy image --exit-code 1 --severity CRITICAL kunchalavikram/trivy-test:v1
trivy image --scanners misconfig kunchalavikram/trivy-test:v1

trivy image --image-config-scanners secret kunchalavikram/trivy-test:v2
trivy image --severity CRITICAL kunchalavikram/trivy-test:v2

trivy image --scanners misconfig --format json kunchalavikram/trivy-test:v1
trivy image --scanners misconfig --format json --output result.json  kunchalavikram/trivy-test:v1





## License

[Apache-2.0 License](LICENSE)
