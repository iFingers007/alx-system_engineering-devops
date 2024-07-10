# Puppet manifest to install and configure Nginx

exec { 'update':
  command => '/usr/bin/apt-get update -y',
}
-> package { 'nginx':
  ensure => 'present',
}
-> file_line { 'Add_Header':
  path  => '/etc/nginx/sites-available/default',
  match => 'server_name _;',
  line  => "server_name _;\n\tadd_header X-Served-By \"${hostname}\";"
}

-> exec { 'start':
  command  => '/usr/sbin/service nginx restart',
}
