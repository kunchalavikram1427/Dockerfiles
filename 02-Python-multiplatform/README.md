# Multi Platform Images

## Using Docker Manifest
```
docker manifest inspect --verbose nginx
docker manifest inspect -v nginx > manifest.json

docker build -t kunchalavikram/python:amd64 --platform linux/amd64 .
docker build -t kunchalavikram/python:arm64 --platform linux/arm64 .
docker push  kunchalavikram/python:arm64
docker push  kunchalavikram/python:amd64
  
docker manifest create kunchalavikram/python:v1  kunchalavikram/python:arm64 kunchalavikram/python:amd64
docker manifest push kunchalavikram/python:v1
docker manifest inspect kunchalavikram/python:v1  > manifest.json

```


## Using BuildX
https://docs.docker.com/build/drivers/docker-container/
```
docker build -t kunchalavikram/singlearch:1.0 .
docker buildx create --name container --driver=docker-container
docker buildx build --push --builder=container --platform linux/amd64,linux/arm64 -t kunchalavikram/multiarch:latest .
docker pull --platform linux/arm64  kunchalavikram/multiarch:latest
docker inspect kunchalavikram/multiarch:latest
```