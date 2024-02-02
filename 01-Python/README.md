docker build -t python:1.0 .

docker run -d --name test -p 8000:8000 python:1.0


docker images
python      1.0      509088963df1   55 seconds ago   478MB
python      2.0      3eb88205bbea   4 seconds ago    66.8MB  


docker build -t python:2.0 -f Dockerfile2 .
docker run -d --name test -p 8000:8000 python:2.0