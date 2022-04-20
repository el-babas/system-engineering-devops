# Install Nginx web server (All previous puppet)

exec {'install Nginx and redirect_me':
  provider => shell,
  command  => 'sudo apt-get -y update ;\
                sudo apt-get -y install nginx ;\
                sudo chown -R ubuntu /var/www ;\
                echo "Hello World" | sudo tee /var/www/html/index.nginx-debian.html ;\
                sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/cristhian1107 permanent;/" \
                    /etc/nginx/sites-available/default ;\
                sudo service nginx start',
}
