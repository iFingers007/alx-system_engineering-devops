# set up your client SSH configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present
  content => "
  # Configuration of client
  host *
  PasswordAuthentication no
  IdentityFile ~/.ssh/school
  "
}
