# Puppet manifest to install and configure Nginx

package { 'nginx':
  ensure => present,
  }

  exec { 'install_nginx':
    command  => 'sudo apt-get update -y; sudo apt-get install -y nginx',
    provider => shell
#    require  => Package['nginx'],
  }

  exec { 'Hello':
    command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
    provider => shell,
#    require  => Exec['install_nginx'],
  }

  exec { 'configure redirect':
    command => 'sudo sed -i "s/server_name _;/server_name _;\n\n\tlocation \/redirect_me {\n\t\t return 301 https:\/\/www.google.com;\n\t}" \
  /etc/nginx/sites-enabled/default',
    provider => shell,
#    require  => Exec['install_nginx'],
  }

  exec { 'Add_Header':
    command  => 'sudo sed -i "27i \\\tadd_header X-Served-By ${HOSTNAME}" /etc/nginx/sites-available/default',
    provider => shell,
    }

  exec { 'start':
    command  => 'sudo service nginx restart',
    provider =>shell,
  }
