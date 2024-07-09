# Puppet manifest to install and configure Nginx

package { 'nginx':
  ensure => present,
}

exec { 'install':
    command  => 'sudo apt-get update -y; sudo apt-get -y nginx',
    provider => shell,
}

file_line { 'Add_Header':
  path  => '/etc/nginx/sites-enabled/default',
  match => 'location / {',
  line  => 'location / {\n\tadd_header X-Served-By \"${hostname}\";',
}

exec { 'start':
  command  => 'sudo service nginx restart',
  provider =>shell,
}
