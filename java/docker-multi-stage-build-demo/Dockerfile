FROM maven:3.6.3-jdk-8 as BUILD
WORKDIR /app
COPY . .
RUN mvn clean package  

FROM openjdk:8-jre-alpine3.9
WORKDIR /app
COPY --from=BUILD /app/target/demo-0.0.1-SNAPSHOT.jar .
ENTRYPOINT ["java", "-jar", "/app/demo-0.0.1-SNAPSHOT.jar"]

