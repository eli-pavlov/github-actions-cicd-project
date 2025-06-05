# Use an official Python runtime as a parent image
FROM python:3.13.4-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app code into the container
COPY src/app.py /app/
COPY templates/index.html /app/templates/

# Install Flask
RUN pip install --no-cache-dir Flask

# Expose the Flask port
EXPOSE 5000

# Define the command to run the Flask app when the container starts
CMD ["python", "app.py"]
