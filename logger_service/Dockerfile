# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all remaining code
COPY . .

# Expose port
EXPOSE 8001

# Run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
