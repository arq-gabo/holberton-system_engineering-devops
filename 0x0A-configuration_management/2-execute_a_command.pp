#Create a manifest that kill a process named killmenow
exec { '/usr/bin/pkill killmenow':
}