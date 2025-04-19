# Use the official Nginx image from the Docker Hub
FROM nginx:stable-alpine

# Remove the default Nginx welcome page.
RUN rm /usr/share/nginx/html/index.html

# Copy the static files from the src directory to the Nginx HTML directory
COPY src/index.html /usr/share/nginx/html/index.html

# Expose port 80 to the outside world
EXPOSE 80

# The base Nginx image already has a CMD instruction, so we don't need to specify one.
# CMD ["nginx", "-g", "daemon off;"] 