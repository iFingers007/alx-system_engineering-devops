# set up your client SSH configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present
}

file_line { 'host_line':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'host *\n',
}

file_line { 'password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no\n'
}

file_line { 'identity':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '/etc/ssh/~/.ssh/school'
}

