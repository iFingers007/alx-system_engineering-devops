# Puppet manifest to install and configure Nginx

package { 'nginx':
  ensure => present,
}

exec { 'install':
  command  => 'sudo apt-get update -y; sudo apt-get -y nginx',
  provider => shell
}

exec { 'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

file_line { 'configure redirect':
  path  => "/etc/nginx/sites-enabled/default",
  match => "server_name _;",
  line  => "server_name _;\n\n\tlocation \/redirect_me {\n\t\t return 301 https:\/\/www.google.com;\n\t}",
}

exec { 'start':
  command  => 'sudo service nginx restart',
  provider =>shell,
}
