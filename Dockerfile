# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set environment variables to prevent Python from writing .pyc files
# and to keep Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies that might be needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Add any system-level dependencies here if needed (e.g., for postgresql client)
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container
COPY . .

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application using Gunicorn
# This is a production-ready WSGI server.
# Replace 'api_project' with the actual name of your Django project directory.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "api_project.wsgi:application"]
