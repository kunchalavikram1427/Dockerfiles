FROM maven AS MAVEN_BUILD 
WORKDIR /app
COPY . .
RUN mvn clean package 

FROM openjdk:11.0.10-jre
WORKDIR /app
COPY --from=MAVEN_BUILD /app/target/zuul-0.0.1-SNAPSHOT.jar .
EXPOSE 9999
CMD ["java", "-jar", "zuul-0.0.1-SNAPSHOT.jar"]
