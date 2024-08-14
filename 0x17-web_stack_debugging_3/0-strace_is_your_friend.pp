# Resolves issues with incorrect phpp file extensions, ensuring they are 
# properly set to php in the WordPress wp-settings.php file.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
