FROM openjdk:8-jre-alpine3.9
WORKDIR /app
COPY target/demo-0.0.1-SNAPSHOT.jar demo.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/demo.jar"]
