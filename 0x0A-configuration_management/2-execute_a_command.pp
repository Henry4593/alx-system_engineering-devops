# This code defines a Puppet exec resource to kill a process named 'killmenow'
exec { 'killmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
