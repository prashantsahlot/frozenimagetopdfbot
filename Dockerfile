# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose server port (optional)
EXPOSE 8080

# Start the bot and dummy server together
CMD ["sh", "-c", "python3 server.py & python3 main.py"]
