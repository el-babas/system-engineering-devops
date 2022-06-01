# Correct TYPO error - debugger.
exec {'typo_errore':
    provider => shell,
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
