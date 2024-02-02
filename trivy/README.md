# Trivy scan

trivy image nginx:latest
trivy image nginx:latest --format json

trivy image nginx:alpine

trivy image nginx:1.19.6

trivy image nginx:1.19.9-alpine

trivy image python:latest

trivy image gcr.io/distroless/python3-debian12	

docker run ghcr.io/aquasecurity/trivy:latest image nginx:latest

docker run ghcr.io/aquasecurity/trivy:latest image nginx:1.19.9-alpine