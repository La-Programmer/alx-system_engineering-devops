# Manage the content of the file /etc/default/nginx
file { 'nginx':
  ensure  => file,
  path    => '/etc/default/nginx',
  content => 'ULIMIT="-n 500"'
}
