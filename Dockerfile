# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app code into the container
COPY app.py /app/
COPY index.html /app/templates/

# Install Flask
RUN pip install --no-cache-dir Flask

# Expose the Flask port
EXPOSE 5000

# Define the command to run the Flask app when the container starts
CMD ["python", "app.py"]2
