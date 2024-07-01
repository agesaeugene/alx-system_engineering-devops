# Executes a command
exec { 'kill_process':
  command  => 'pkill -f killmenow',
  provider => 'shell',
  path     => ['/usr/bin', '/usr/sbin',]
}
