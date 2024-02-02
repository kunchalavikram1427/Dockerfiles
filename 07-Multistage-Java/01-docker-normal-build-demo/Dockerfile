FROM maven:3.6.3-jdk-8 
WORKDIR /app
COPY . .
RUN mvn clean package 
EXPOSE 8080
CMD ["java", "-jar", "target/demo-0.0.1-SNAPSHOT.jar"]
