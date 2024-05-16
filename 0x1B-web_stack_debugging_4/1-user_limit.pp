# Create a new user
user { 'holberton':
  ensure   => present,
  uid      => 1001,
  gid      => 1001,
  home     => '/home/holberton',
  shell    => '/bin/bash',
  password => 'j1u2s3t4i5n6',
}
