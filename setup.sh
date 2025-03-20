#!/bin/sh
sudo dnf update -y
echo "Start Install Apache: "
sudo dnf install httpd -y
echo ""
echo "Start Install Python: "
sudo dnf install python3 -y
python3 --version
echo ""
echo "Start Install PHP: "
sudo dnf install php php-cli php-common php-fpm php-mysqlnd -y
php -v
echo ""
echo "Start Web Server: "
sudo systemctl start httpd

sudo cp src/* /var/www/html
echo "Copied src files to /var/www/html"
