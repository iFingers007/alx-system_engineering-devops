# set up your client SSH configuration file

file_path = '/etc/ssh/ssh_config'
file { $file_path
  ensure  => present,
  content => "
  # Configures file
  host *
  PasswordAuthentication no\n
  IdentityBy /etc/ssh/ssh_config\n
  "
}
