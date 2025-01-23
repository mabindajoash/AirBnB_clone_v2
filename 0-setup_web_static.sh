#!/usr/bin/env bash
# set up servers for deployment
sudo apt-get install nginx -y
mkdir /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<h2>test nginx configuration</h2>" > /data/web_static/releases/test/index.html
ln -s /data/webstatic/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
	alias /data/web_static/current;
	index index.html index.htm;
    }

    location /redirect_me {
    	return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
								    }
}" > /etc/nginx/sites-available/default

sudo service reload nginx
