# Use official Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first for caching dependencies
COPY logger_service/requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the service code
COPY logger_service/ .

# Expose FastAPI default port
EXPOSE 8001

# Start FastAPI server with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
