# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /workspace

# Install necessary packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the current application code into the container
COPY . .

# Expose a port (needed for debugging)
EXPOSE 5678

# Start command for the container
CMD ["python", "app.py"]
