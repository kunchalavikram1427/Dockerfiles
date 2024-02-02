FROM python:alpine3.19
RUN pip install --no-cache-dir flask
WORKDIR /app
COPY . .
EXPOSE 5000
CMD ["python","/app/main.py"]