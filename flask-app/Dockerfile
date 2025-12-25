# Python flask App

Simple flask application
ubuntu@ip-172-31-14-42:~/flask-app$ cat Dockerfile
# 1. Base image (OS)

FROM python:3.9-slim

# 2. Working directory

WORKDIR /app

# 3. Copy the code from HOST (source) to the working directory

COPY . .

# 4. Run the build command

RUN pip install -r requirements.txt

# 5. Expose the port

EXPOSE 80

# 6. Server the app / run the app (Keep it running)

CMD ["python","run.py"]
