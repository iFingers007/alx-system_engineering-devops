# Puppet manifest to install and configure Nginx

package { 'nginx':
  ensure => present,
  }

  exec { 'install':
    command => 'sudo apt-get update -y; sudo apt-get -y nginx',
    provider => shell
  }

  exec { 'Hello':
    command => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
    provider => shell,
  }

  exec {'sudo sed -i "s/server_name _;/server_name _;\n\n\tlocation \/redirect_me {\n\t\t return 301 https:\/\/www.google.com;\n\t}" \
/etc/nginx/sites-enabled/default':
  provider => shell,
  }

  exec { 'start':
    command => 'sudo service nginx restart',
    provider =>shell,
  }
