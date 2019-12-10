# Using Puppet for create the file holberton in the directory /tmp
file { '/tmp/holberton':
path    =>'/tmp/holberton',
mode    =>'0744',
owner   =>'www-data',
group   =>'www-data',
content =>'I love Puppet',
}
