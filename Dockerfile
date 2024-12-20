FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the application port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["python", "run.py"]