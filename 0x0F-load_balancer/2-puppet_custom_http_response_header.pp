# Puppet manifest to install and configure Nginx

package { 'nginx':
  ensure => present,
}

exec { 'install':
  command  => 'sudo apt-get update -y; sudo apt-get -y nginx',
  provider => shell,
}

exec { 'Add_Header':
  command  => "sudo sed -i '55i \\\t\\\tadd_header X-Served-By \"${hostname}\";' /etc/nginx/sites-available/default",
  provider => shell,
}

exec { 'config':
  command  => 'sudo nginx -t',
  provider => shell,
}

exec { 'start':
  command  => 'sudo service nginx restart',
  provider =>shell,
}
