# make changes to 'ssh_config' file using puppet codes
# Define a class for managing SSH client configuration
class { 'ssh::client': }

# Configure IdentityFile
file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile  ~/.ssh/school',
  match  => absent,
}

# Disable PasswordAuthentication
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => absent,
}
