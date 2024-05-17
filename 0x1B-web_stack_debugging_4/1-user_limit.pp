# Fix OS config
exec {
  'fix os config':
  command => '/bin/sed -i "s/5/2048/g; s/4/1024/g" /etc/security/limits.conf',
  path    => '/bin/',
  unless  => '/bin/grep -q "holberton hard nofile 2048"',
}
