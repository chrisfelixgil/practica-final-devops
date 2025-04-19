# Use the official Nginx image from the Docker Hub
FROM nginx:stable-alpine

# Remove the default Nginx welcome page.
RUN rm /usr/share/nginx/html/index.html

# Copy the static file from the root directory to the Nginx HTML directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 to the outside world
EXPOSE 80
