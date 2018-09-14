Разберем установку postfixadmin с базовой настройкой и созданием скрипта для  этих целей. 



1 Нужно установить базу данных. Я возьму стандартную MariaDB

```

apt install myaql-server -y   

```

Все остальные сранные  пакеты подтянутся. Далее настраиваем MariaDB  

```

mysql_secure_installation

```

Устанавливаем root пароль, все остальное "Да"



2 Создаем базу данных для postfixadmin, все таблицы он создаст сам. 

```

 mysql -u root -p ( далее ввести пароль root в mysql )

CREATE USER 'postfixadmin'@'localhost' IDENTIFIED BY 'mypass';

GRANT USAGE ON *.* TO 'postfixadmin'@'localhost' IDENTIFIED BY 'mypass';

CREATE DATABASE IF NOT EXISTS `dbname`;

GRANT ALL PRIVILEGES ON `dbname`.* TO 'dbuser'@'localhost';

FLUSH PRIVILEGES;

```

3 Нам нужен nginx +  php-fpm (часть джентельменского набора )



```

apt install nginx php-fpm -y

```

Уповаю в надежне на то что все пакеты установились...



4   Качаем и расспаковуем postfixadmin 



```

apt install unzip

mkdir /var/www/postfixadmin

cd /var/www/postfixadmin/ 

wget https://github.com/postfixadmin/postfixadmin/archive/postfixadmin-3.1.zip

unzip postfixadmin-3.1.zip

rm postfixadmin-3.1.zip

mv postfixadmin-postfixadmin-3.1/* ./

rm -rf postfixadmin-postfixadmin-3.1/

rm  /etc/nginx/sites-enabled/*



```



Далее редактируем настройки nginx:



```

 server{

        listen  80;

        server_name _;

    access_log /var/log/nginx/postfixadmin_access.log;

    error_log /var/log/nginx/postfixadmin_error.log;

    root   /var/www/;

    index index.php;

          location ~* \.(jpg|jpeg|gif|png|bmp|ico|pdf|flv|swf|exe|html|htm|txt|css|js)$ {

    root /var/www/;

    }



    location /postfixadmin {

    try_files $uri $uri/ /index.php?$args;

    auth_basic "Please, enter login and password";

    auth_basic_user_file    "/var/www/alex/.htpasswd";

    }





        location ~ \.php$ {

        fastcgi_pass unix:/run/php/php7.0-fpm.sock;

        include fastcgi_params;

        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;

        }



        location ~ /\.ht {

              deny all;

        }

}

``` 

Postfixadmin

Скачиваем с оф сайта postfixadmin

http://postfixadmin.sourceforge.net/

Устанавливаем и настраиваем postfixadmin

Распаковывем архив в нужную директорию на сервере и настраиваем apache, nginx,...



Редактируем в файле config.inc.php в корне postfixadmin такие строки:

```

$CONF['database_type'] = 'mysql';

$CONF['database_host'] = 'localhost';

$CONF['database_user'] = 'postfixadmin'; установить имя пользователя к бд

$CONF['database_password'] = '123'; установить пароль к бд

$CONF['database_name'] = 'postfixadmin'; установить имя бд

//по дефолту имеет значение&nbsp;INBOX.; лучше убрать, чтобы не было проблем с автосозданием папок

$CONF['database_prefix'] = '';

```

Далбратиться в браузере к postfixadmin, например так

http://mydomainname/postfixadmin/setup.php

и выполнить все требования postfixadmin-a если чего-то не хватает в системе. Будет предложено создать аккаунт админа для postfixadmin и выведен хэш, который надо будет вписать в соответствующую строку config.inc.php

```

$CONF['setup_password'] = ' ';

```

В старых версиях pfa требовалось удалять setup.php, в новых это не требуется.

Можно сразу войти в postfixadmin и создать домен и почтовый ящик для дальнейшей работы. При этом только будут созданы записи в бд, директориии на диске будут созданы только после того как dovecot попытается доставить в них полученную почту.





Финальные штрихи 



```

apt install php-mysqli php-mbstring

 ln -s /etc/nginx/sites-available/postfixadmin.conf /etc/nginx/sites-enabled/postfixadmin.conf

service nginx restart

mkdir /var/www/postfixadmin/templates_c



chmod -R 777 /var/www/postfixadmin/

```



 