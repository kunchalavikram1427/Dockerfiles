FROM python:3.9.7-alpine3.14
RUN pip install flask flask_sqlalchemy pymysql
WORKDIR /app
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]