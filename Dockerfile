# ./sentive_saas/Dockerfile
# We Use an official Python runtime as a parent image
FROM python:3.8-slim

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
# set environment variables for Django configuration
ENV DJANGO_SETTINGS_MODULE "sentive_saas.settings"
ENV DJANGO_CONFIGURATION "Dev"

# create root directory for our project in the container
#RUN mkdir /sentive_saas
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
ADD . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#Expose to port
#provide port access to docker system so other container can access the service by this port.
#expose only publish the port within docker system, so host computer service or app can not get this port to access service.
#EXPOSE 8000

# copy project
COPY . /app
CMD exec gunicorn sentive_saas.wsgi:application — bind 0.0.0.0:8000 — workers 3
