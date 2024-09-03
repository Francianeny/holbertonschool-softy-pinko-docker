# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install Flask and Flask-CORS
RUN pip install flask flask-cors

# Copy the backend application files
COPY ./api.py /app/api.py

# Set the environment variable for Flask
ENV FLASK_APP=api.py

# Expose port 5252
EXPOSE 5252

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5252"]
