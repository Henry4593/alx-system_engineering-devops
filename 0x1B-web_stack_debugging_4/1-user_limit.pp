# Configure user 'holberton' for proper file access.

# Increase the hard file limit for the Holberton user to 50000.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => '/bin/sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin'}

# Increase the soft file limit for the Holberton user to 50000.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => '/bin/sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin'}
