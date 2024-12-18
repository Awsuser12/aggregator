# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt first to leverage Docker's cache for faster builds
COPY requirements.txt /app/

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Uvicorn as it's required to run the app
RUN pip install uvicorn

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port your app will run on (e.g., 8000 for Uvicorn)
EXPOSE 8000

# Set the command to run the application using Uvicorn
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
