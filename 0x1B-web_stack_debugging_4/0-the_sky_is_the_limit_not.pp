# increase the amount of traffic an nginx server can handle

# Increases the ULIMIT of the default file
exec { 'fix--for-nginx':
  # updates the ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # Specifies the path for the sed command
  path	  => '/usr/local/bin/:/bin/',
}

# Restart nginx
exec { 'nginx-restart':
  # Restart Nginx sevice
  command => '/etc/init.d/nginx restart',
  # Specifying the path for init.d script
  path => '/etc/init.d/',
}
