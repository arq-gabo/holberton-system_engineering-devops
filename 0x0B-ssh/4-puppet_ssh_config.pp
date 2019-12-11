#File of configuration with puppet
exec { 'line':
command  =>'/bin/echo -e "PasswordAuthentication no IdentityFile ~/.ssh/holberton" >> ~/.ssh/ssh_config',
path     =>'/usr/bin'
}