ARG TAG=3.9.6-amazoncorretto-17
FROM maven:${TAG} as BUILD
WORKDIR /app
COPY . .
RUN mvn package

FROM amazoncorretto:17-al2023-headless
WORKDIR /app
COPY --from=BUILD /app/target/spring-petclinic-3.2.0-SNAPSHOT.jar ./demo.jar
EXPOSE 8080
CMD ["java", "-jar", "/app/demo.jar"]