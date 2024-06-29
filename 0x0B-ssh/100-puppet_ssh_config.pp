# set up your client SSH configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present
}

file_line { 'host':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  match  => '^host*',
  line   => 'host*'
}

file_line { 'password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  match  => '^ PasswordAuthentication',
  line   => 'PasswordAuthentication no',
}

file_line { 'identity_file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  match  => '^IdentityFile',
  line   => 'IdentityFile ~/.ssh/school',
}
  
