Plesk
----



Update in the test aria CMS Joomla and  Wordpress for latest stable version. Change version of php from 5.4 to 7.X.

Включаем кастомный PHP
```
/usr/local/psa/bin/php_handler --add -displayname <NN> -path <path to php cgi> -phpini <path to php.ini> -type <php handler> -id <NN-custom> -clipath <path to php cli>

 /usr/local/psa/bin/php_handler --add -displayname 5.6 -path /usr/bin/php-cgi -phpini /etc/php/5.6/fpm/php.ini -type fastcgi -id 56-custom -clipath /usr/bin/php5.6
 public $dbprefix = 'jos_';


 /usr/local/psa/bin/php_handler --add -displayname 5.6 -path /usr/sbin/php-fpm5.6 -phpini /etc/php/5.6/fpm/php.ini -type fpm -old-id 56-custom -new-id 56-php -clipath /usr/bin/php5.6
```
Росстановление из бекапа 

plesk bin pleskrestore --restore "Backup-file" -only-databases

plesk bin pleskrestore --restore "backup_1709080133.tar" -only-sites monsiberien.com

 /usr/local/psa/bin/pleskrestore –create-map /var/lib/psa/dumps/domains/sd-55100.dedibox.fr/backup_user-data_1709080133.tgz -map mapfilename


plesk bin pleskrestore --restore /var/lib/psa/dumps/domains/sd-55100.dedibox.fr/backup_user-data_1709080133.tgz -level domains -filter list:monsiberien.com  -ignore-sign 

 	 plesk bin pleskrestore --restore backup_1709080133.tar -level domains -ignore-sign 

```
UPDATE `jos_users` 
SET `password` = MD5('new_password') 
WHERE `username` = 'admin'
```
Cn2o2@u8

groupe-titan.fr it takes up 100 gigabytes of space, I see all sorts of archives and files that are not related to the site. 
titan_group
Khep2*39
PassivePorts 49152 65535