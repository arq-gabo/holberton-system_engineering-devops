#Create a manifest that kill a process named killmenow
file { 'killmenow' :
ensure   =>'exec',
content  =>'pkill',
}