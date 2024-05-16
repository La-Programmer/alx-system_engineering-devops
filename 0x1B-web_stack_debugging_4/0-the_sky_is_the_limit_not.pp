# Fix NginX web server to be able to handle many requests 
exec { 'fix -- for nginx':
  # modify the ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # Specify the correct path for the sed command
  path    => '/bin/',
  # Ensure that the command only runs when necessary
  unless  => '/bin/grep -q "ulimit -n 4096" /etc/default/nginx',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Exec['fix -- for nginx'],  # Ensure Nginx is restarted only after ULIMIT is modified
}
