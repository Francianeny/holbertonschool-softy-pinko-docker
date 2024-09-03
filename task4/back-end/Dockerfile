# Dockerfile for task4 back-end
FROM python:3.8-slim

# Install Flask and Flask-Cors
RUN pip install flask flask-cors

# Set working directory
WORKDIR /app

# Copy the API script
COPY ./api.py /app/api.py

# Expose port
EXPOSE 5252

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5252"]
