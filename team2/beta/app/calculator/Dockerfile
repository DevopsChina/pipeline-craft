FROM maven:3.5-jdk-8-alpine

COPY ./pom.xml /bmi/
COPY ./calculator /bmi/calculator

WORKDIR /bmi/calculator
RUN mvn clean package

EXPOSE 7777

ENTRYPOINT ["java", "-jar", "/bmi/calculator/target/bmi-calculator-2.6.0.jar"]
