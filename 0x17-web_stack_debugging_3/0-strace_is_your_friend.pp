  
#Puppet for a wordpress installation
exec { '/var/www/html/wp-settings.php':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => 'shell'
}