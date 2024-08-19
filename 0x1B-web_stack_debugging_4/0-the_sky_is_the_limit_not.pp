# increases traffic threshold for nginx

# Increase the ULIMIT of the nginx
exec { 'increase-user-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# restarts nginx
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
