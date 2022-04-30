FROM python:latest
RUN pip install flask flask_cors
WORKDIR /app
COPY index.py .
EXPOSE 5000
ENTRYPOINT ["python", "index.py"] 