# Creates/modifies my etc/ssh/ssh_config

file { '/etc/ssh/ssh_config':
    ensure  => file,
    mode    => '0600',
    owner   => 'justin',
    content => 'Host *
    PasswordAuthentication no
    CertificateFile /home/justin/.ssh/school'
}
