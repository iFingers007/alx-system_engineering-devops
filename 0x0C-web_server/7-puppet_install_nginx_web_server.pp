# Puppet manifest to install and configure Nginx

class nginx_setup {

  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    require    => Package['nginx'],
  }

  # Create the index.html file with "Hello World!" content
  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  # Create the custom 404 error page
  file { '/var/www/html/custom_404.html':
    ensure  => file,
    content => 'Ceci n\'est pas une page',
    require => Package['nginx'],
  }

  # Configure the Nginx default site directly in the manifest
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    server_name _;

    location /redirect_me {
        return 301 https://www.google.com;
    }

    location / {
        try_files $uri $uri/ =404;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        internal;
    }
}
',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Ensure the configuration is symlinked to sites-enabled
  file { '/etc/nginx/sites-enabled/default':
    ensure => link,
    target => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
  }

}
