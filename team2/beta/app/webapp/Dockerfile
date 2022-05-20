FROM maven:3.5-jdk-8-alpine

COPY ./pom.xml /bmi/
COPY ./webapp /bmi/webapp

WORKDIR /bmi/webapp

RUN mvn clean package

EXPOSE 8889

ENTRYPOINT ["java", "-jar", "/bmi/webapp/target/bmi-webapp-2.6.0.jar"]

