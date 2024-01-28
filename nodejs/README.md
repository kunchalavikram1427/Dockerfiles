Build Image:
docker build . -t node-web-app:1.0

Run the Image:
docker run -p 8080:8080 -d node-web-app:1.0
