# Manage the content of the file /etc/default/nginx
file { 'nginx':
  path    => '/etc/default/nginx',
  ensure  => file,
  content => 'ULIMIT="-N 500"'
}
