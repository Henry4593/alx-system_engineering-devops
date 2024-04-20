# make changes to 'ssh_config' file using puppet codes
file { '/etc/ssh/ssh_config':
  # Ensure the file is present
  ensure => present,
  # Define the content of the file
  content => <<EOF
# SSH client configuration
Host *
  # Use the SSH key from ~/.ssh/school
  IdentityFile  ~/.ssh/school
  # Disable password authentication
  PasswordAuthentication no
EOF
  # Owner and group permissions (optional)
  # owner => 'root',
  # group => 'root',
  # File permissions (optional)
  # mode => '0644',
}

