FROM maven  AS MAVEN_BUILD 
WORKDIR /app
COPY . .
RUN mvn clean package 

FROM openjdk:11.0.10-jre
WORKDIR /app
COPY --from=MAVEN_BUILD /app/target/shoes-0.0.1-SNAPSHOT .
EXPOSE 1002
CMD ["java", "-jar", "shoes-0.0.1-SNAPSHOT"]
