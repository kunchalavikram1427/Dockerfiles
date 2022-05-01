# we will use openjdk 8 with alpine as it is a very small linux distro
FROM openjdk:8-jre-alpine3.9
# Set Working directory
WORKDIR /app
# copy the packaged jar file into our docker image
COPY target/demo-0.0.1-SNAPSHOT.jar demo.jar
# execute the jar
ENTRYPOINT ["java", "-jar", "/app/demo.jar"]
