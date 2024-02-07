ARG TAG=3.9.6-amazoncorretto-17
FROM maven:${TAG}
WORKDIR /app
COPY . .
RUN mvn package
EXPOSE 8080
CMD ["java", "-jar", "/app/target/*.jar"]