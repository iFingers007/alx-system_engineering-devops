# set up your client SSH configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
  # Configures file
  host*\n
  PasswordAuthentication no\n
  IdentityFile /etc/ssh/~/.ssh/school\n
  "
}
