# Use Python slim image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for Flask
EXPOSE 5000

# Command to run the Flask application
CMD ["python3", "app.py"]
