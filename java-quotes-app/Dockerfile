# 1. Base image (OS)

FROM eclipse-temurin:17-jdk-alpine

# 2. Working directory for the app inside the container

WORKDIR /app

# 3. Copy the code from the HOST to the container working directory i.e. /app

COPY src/Main.java /app/Main.java

COPY quotes.txt quotes.txt

# 4. Run the commands to install the libraries or to compile the code

RUN javac Main.java

# 5. Expose the port

EXPOSE 8000

# Serve the app / Keep it running

CMD ["java","Main"]
