# Use Python 3.6.3 as a base image
FROM python:3.8

# Make a directory called "code" which will contain the source code. This will be used as a volume in our docker-compose.yml file
RUN mkdir /app

COPY . /app

# Set the working directory for the container. I.e. all commands will be based out of this directory
WORKDIR /app

# Install all dependencies required for this project. the trusted-host flag is useful if you are behind a corporate proxy.
RUN pip3 install -r /app/requirements.txt