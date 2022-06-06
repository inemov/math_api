# syntax=docker/dockerfile:1
# set base image
FROM python:3.8-slim
# set the working directory in the container
WORKDIR /app
# copy the dependencies list to the working directory
COPY requirements.txt .
# install dependencies
RUN pip3 install -r requirements.txt
# copy content of the source code folder to the working directory
COPY src/ .
# run on container start
CMD ["python3", "./app.py"]

