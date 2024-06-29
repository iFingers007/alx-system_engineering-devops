# set up your client SSH configuration file


file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
  # Configures file
  host *
  PasswordAuthentication no\n
  IdentityBy /etc/ssh/ssh_config\n
  "
}
