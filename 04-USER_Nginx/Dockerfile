FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user to run Nginx
ARG USER_ID=1000
ARG GROUP_ID=1000

# Create a non-root user to run Nginx
RUN groupadd -g $GROUP_ID appuser && \
    useradd -u $USER_ID -g $GROUP_ID -M -s /bin/bash appuser

# Change ownership of necessary directories to the new user
RUN chown -R appuser:appuser /var/log/nginx /var/lib/nginx /var/run /run

USER appuser
# Expose port 80 for Nginx
EXPOSE 80
# Command to start Nginx
CMD ["nginx", "-g", "daemon off;"]