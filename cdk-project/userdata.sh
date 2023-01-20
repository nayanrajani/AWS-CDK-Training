#!/bin/bash

yum update -y
yum install httpd -y
sudo service httpd start
echo "<h2>Welcome AWS $(hostname -f) </h2><hr>" >  /var/www/html/index.html
curl http://169.254.169.254/latest/meta-data/instance-id >> /var/www/html/index.html