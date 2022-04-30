FROM maven:3.6.3-jdk-8  AS MAVEN_BUILD 
WORKDIR /app
COPY . .
RUN mvn clean package 

FROM openjdk:11.0.10-jre
WORKDIR /app
COPY --from=MAVEN_BUILD /app/target/offers-0.0.1-SNAPSHOT .
EXPOSE 1001
CMD ["java", "-jar", "offers-0.0.1-SNAPSHOT"]
