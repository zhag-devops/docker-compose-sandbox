# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container and install the dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 5000 for the Flask app
EXPOSE 5050

# Define environment variable
ENV FLASK_APP=app.py

# Run the command to start the Flask app when the container launches
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5050"]
