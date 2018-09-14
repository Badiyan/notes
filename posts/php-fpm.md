Моя шпаргалка по PHP-FPM 



```

I extended limits:

nginx: fastcgi_read_timeout 120



php-fpm:

pm.start_servers = 5

pm.min_spare_servers = 5

pm.max_children = 20

pm.max_spare_servers = 15

pm.max_requests =700



php memory_limit: 1024

define( 'WP_MEMORY_LIMIT', '512M' ); into config /var/www/wordpress/domains/amika.com.hk/wp-config.php



And set instance tipe: t2.large



```