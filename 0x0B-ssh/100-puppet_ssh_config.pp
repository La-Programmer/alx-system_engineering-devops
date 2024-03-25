# Creates/modifies my ~/.ssh/config

file { '/home/justin/.ssh/config':
    ensure  => file,
    mode    => '0600',
    owner   => 'justin',
    content => 'Host *
                    PasswordAuthentication no
                    CertificateFile /home/justin/.ssh/school'
}
