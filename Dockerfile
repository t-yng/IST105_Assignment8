FROM php:8.2-apache

# Install Python3 and PHP dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && docker-php-ext-install pcntl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html
COPY src/ .

# Add execute permission to process_input.py
RUN chmod +x network_config.py

EXPOSE 80
