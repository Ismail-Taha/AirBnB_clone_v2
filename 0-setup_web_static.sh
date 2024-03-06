#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Update and install Nginx if it's not already installed
apt-get update
apt-get install -y nginx

# Allow 'Nginx HTTP' through the firewall, uncomment if firewall is enabled and needs configuration
# ufw allow 'Nginx HTTP'

# Create the necessary directories
mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file to test your Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link, force creation to ensure it’s updated if it already exists
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ under hbnb_static
sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/; index index.html index.htm; }' /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
service nginx restart
