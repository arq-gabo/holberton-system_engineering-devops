#File of configuration with puppet
exec { 'line':
command =>'/bin/echo -e "PasswordAuthentication no\n IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
path    =>'/usr/bin'
}