# Puppet manifest to install and configure Nginx

package { 'nginx':
  ensure => present,
  }

  file_line { 'Add_Header':
    path  => '/etc/nginx/sites-available/default',
    match => 'location /',
    line  => 'location /\n\tadd_header X-Served-By \"${hostname}\";',
    }

  exec { 'start':
    command  => 'sudo service nginx restart',
    provider =>shell,
  }
