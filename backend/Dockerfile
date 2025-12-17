# backend/Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app/backend

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/backend
COPY . /app/backend

# Expose the port that FastAPI runs on
EXPOSE 8000

# Run the FastAPI application using Uvicorn
# Make sure to adjust `main:app` to your actual FastAPI application instance
# and `0.0.0.0` to listen on all available network interfaces.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
