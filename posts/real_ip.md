Обычной задачей при настройке связки Nginx + Apache, являетя обеспечение правильного значения переменной REMOTE_ADDR (в ней должен содержаться реальный IP клиента, а не локальный IP сервера).



Эта проблема решается установкой модулей rpaf или remoteip и небольшими правками конфигурационных фалов Nginx, а в случае использования панели управления веб хостингом Vesta CP — ее шаблонов.



Сначала, в панели управления Vesta CP в разделе управления доменами отключается поддержка Proxy NGINX, чтобы старые настройки корректно удалились из /home/user/conf/web/nginx.conf.

Затем, в шаблоны Vesta CP отвечающие за настройку Nginx, в секцию location, добавляется установка следующих заголовков:

```

proxy_set_header Host $host;

proxy_set_header X-Real-IP $remote_addr;

proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

```

Редактируем шаблоны Proxy default

```

vi /usr/local/vesta/data/templates/web/nginx/default.tpl

```



```

server {

    listen      %ip%:%proxy_port%;

    server_name %domain_idn% %alias_idn%;

    error_log  /var/log/%web_system%/domains/%domain%.error.log error;

 

    location / {

        proxy_set_header Host $host;

        proxy_set_header X-Real-IP $remote_addr;

        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

 

        proxy_pass      http://%ip%:%web_port%;

        location ~* ^.+\.(%proxy_extentions%)$ {

            root           %docroot%;

            access_log     /var/log/%web_system%/domains/%domain%.log combined;

            access_log     /var/log/%web_system%/domains/%domain%.bytes bytes;

            expires        max;

            try_files      $uri @fallback;

        }

    }

 

    location /error/ {

        alias   %home%/%user%/web/%domain%/document_errors/;

    }

 

    location @fallback {

        proxy_pass      http://%ip%:%web_port%;

    }

 

    location ~ /\.ht    {return 404;}

    location ~ /\.svn/  {return 404;}

    location ~ /\.git/  {return 404;}

    location ~ /\.hg/   {return 404;}

    location ~ /\.bzr/  {return 404;}

 

    include %home%/%user%/conf/web/nginx.%domain%.conf*;

}

```

```

vi /usr/local/vesta/data/templates/web/nginx/default.stpl

```

```

server {

    listen      %ip%:%proxy_ssl_port%;

    server_name %domain_idn% %alias_idn%;

    ssl         on;

    ssl_certificate      %ssl_pem%;

    ssl_certificate_key  %ssl_key%;

    error_log  /var/log/%web_system%/domains/%domain%.error.log error;

 

    location / {

        proxy_set_header Host $host;

        proxy_set_header X-Real-IP $remote_addr;

        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

 

        proxy_pass      https://%ip%:%web_ssl_port%;

        location ~* ^.+\.(%proxy_extentions%)$ {

            root           %sdocroot%;

            access_log     /var/log/%web_system%/domains/%domain%.log combined;

            access_log     /var/log/%web_system%/domains/%domain%.bytes bytes;

            expires        max;

            try_files      $uri @fallback;

        }

    }

 

    location /error/ {

        alias   %home%/%user%/web/%domain%/document_errors/;

    }

 

    location @fallback {

        proxy_pass      https://%ip%:%web_ssl_port%;

    }

 

    location ~ /\.ht    {return 404;}

    location ~ /\.svn/  {return 404;}

    location ~ /\.git/  {return 404;}

    location ~ /\.hg/   {return 404;}

    location ~ /\.bzr/  {return 404;}

 

    include %home%/%user%/conf/web/snginx.%domain%.conf*;

}

```

Включаем поддержку Proxy NGINX в панели управления, и в /home/user/conf/web/nginx.conf будут записаны настройки согласно измененным шаблонам.

Включаем модуль rpaf



```

a2enmod rpaf

```

и вносим изменения в его настройки

```

vi /etc/apache2/mods-enabled/rpaf.conf

```

```

<IfModule rpaf_module>

    RPAFenable On

 

    # When enabled, take the incoming X-Host header and

    # update the virtualhost settings accordingly:

    RPAFsethostname On

 

    # Define which IP's are your frontend proxies that sends

    # the correct X-Forwarded-For headers:

    RPAFproxy_ips 127.0.0.1 ::1 IP_адрес_сервера

 

    # Change the header name to parse from the default

    # X-Forwarded-For to something of your choice:

    # RPAFheader X-Real-IP

</IfModule>

```

Или включаем модуль remoteip

```

a2enmod remoteip

```

и создаем файл с его настройками

```

vi /etc/apache2/mods-enabled/remoteip.conf

```

```

<IfModule mod_remoteip.c>

   #  RemoteIPHeader X-Forwarded-For

      RemoteIPHeader X-Real-IP

      RemoteIPInternalProxy IP_адрес_сервера

</IfModule>

```

После включения модуля и изменения конфига нужно перезапустить Apache:

```

service apache2 restart

```

Если придется вручную исправлять файлы настроек nginx для конкретных доменов, то для вступления настроек в силу нужно перезапустить Nginx:

```

service nginx restart

```

http://mppks.ru/vds/pravilnyiy-remote_addr-v-nginx-apache/



####Способ №2 

Этот способ помог настроить ввсе правильно 

```

Ubuntu 14.04 лечится добавленим конфигов модуля



Некоректное определение ip:

sudo nano /etc/apache2/mods-enabled/rpaf.conf

<IfModule rpaf_module>

RPAFenable On

RPAFsethostname On

RPAFproxy_ips 111.222.333.444

RPAFheader X-Real-IP

</IfModule>



sudo nano /home/andrianov/conf/web/nginx.conf

location / {

proxy_pass http://111.222.333.444:8080;

proxy_set_header Host $host;

proxy_set_header X-Real-IP $remote_addr;

proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;



проверка ip



если ip продолжает неправильно определятся то 



sudo nano /etc/apache2/mods-enabled/remoteip.conf

добавить

<IfModule remoteip_module>

RemoteIPHeader X-Real-IP

</IfModule>



sudo nano /etc/apache2/mods-enabled/remoteip.load

добавить

LoadModule remoteip_module /usr/lib/apache2/modules/mod_remoteip.so

```