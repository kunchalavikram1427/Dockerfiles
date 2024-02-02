docker build -t kunchalavikram/singlearch:1.0 .

docker buildx create --name container --driver=docker-container

docker buildx build --push --builder=container --platform linux/amd64,linux/arm64 -t kunchalavikram/multiarch:latest .

docker pull --platform linux/arm64  kunchalavikram/multiarch:latest

docker inspect kunchalavikram/multiarch:latest

https://docs.docker.com/build/drivers/docker-container/