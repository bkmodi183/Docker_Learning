# Base image (OS)

FROM node:18-alpine

# Working directory

WORKDIR /app

# Copy the code from source to container working directory

COPY . .

# Install the build

RUN npm install && npm build

# Expose the port

EXPOSE 3000

# Server the application

CMD ["npm","run","dev"]
