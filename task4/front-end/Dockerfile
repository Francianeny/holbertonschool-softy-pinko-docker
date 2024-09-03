# Dockerfile for task4 front-end
FROM nginx:latest

# Copy the HTML files into the container
COPY ./softy-pinko-front-end /usr/share/nginx/html

# Copy the nginx configuration
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf
