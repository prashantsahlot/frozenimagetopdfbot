# Use official Python slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies for building wheels and git
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Expose port for uptime server
EXPOSE 8080

# Start both server and bot
CMD ["python3", "FrozenConverter/bot.py"]


