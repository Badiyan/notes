Задачки на тестовое задание
----

```

Тестовые задания:



Задание 1:

Имеется лог nginx в формате combined. Нужно считать следующую статистику и сохранить в файл:

a) top10 ip адресов

b) top10 URL

c) top10 юзерагентов

Приложить скрипты и команды.

Пример лога:

111.111.111.11 ­ ­ [02/Jun/2017:10:34:15 ­0400] "GET /analytics/tracker/tab/?id=876400 HTTP/1.0" 200 0 "http://example.com/p/phil_wickham/cielo_crd.htm" "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"

121.121.121.21 ­ ­ [02/Jun/2017:10:34:15 ­0400] "GET /analytics/tracker/tab/?id=24655 HTTP/1.0" 200 0 "http://example.com/l/lynyrd_skynyrd/sweet_home_alabama_intro_tab.htm" "Mozilla/5.0 (X11; CrOS x86_64 6812.88.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.153 Safari/537.36"

131.131.131.31 ­ ­ [02/Jun/2017:10:34:15 ­0400] "GET /analytics/tracker/tab/?id=88419 HTTP/1.0" 200 0 "http://example.com/y/yardbirds/mr_your_a_better_man_than_i_crd.htm" "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"

141.141.141.41 ­ ­ [02/Jun/2017:10:34:15 ­0400] "GET /analytics/tracker/tab/?id=1481746 HTTP/1.0" 200 0 "http://example.com/m/michael_jackson/billie_jean_ver4_tab.htm" "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko"



Задание 2:

Имеется 1 сервер с nginx и 3-ри сервера с php-fpm

Нужно сделать конфиг для nginx который выступает в качестве load balancer'а для backend серверов. 



Конфигурации должно быть две

1) Алгоритм балансировки round robin, все запросы равномерно распределяется на все 3-ри сервера

2) Алгоритм балансировки round robin, на первый сервер уходит 50% запросов, а на второй и третий по 25%



Так же если один из backend серверов отдал ошибку (500, 502, 504) один раз за 1 секунду, то запросы на него должны переставать отправляться и распределятся между оставшимися серверами.





Задание 3:

Нужно запретить доступ к сайтам с user-agent Firefox и Chrome, но если у пользователя ip адрес 8.8.8.8, то доступ нужно разрешить

Вместо 8.8.8.8 можно использовать свой домашний ip.

Сделать нужно в конфиге nginx



Смотреть нужно в сторону map и if в nginx. Так же можно придумать вариант с использованием set



Может пригодится документация и Google :)

http://nginx.org/ru/docs/http/ngx_http_map_module.html

http://nginx.org/ru/docs/http/ngx_http_rewrite_module.html#if

http://nginx.org/ru/docs/http/ngx_http_rewrite_module.html#set



Задание 4:

имеется файл с содержимым вида:

username1

somepass

8.8.8.8

user2

pass2

127.0.0.1



Нужно командой или скриптом привести данный файл к виду:

username1:somepass 8.8.8.8

user2:pass2 127.0.0.1



Команда или скрипт должны корректно обработать любое количество записей.



Задание 5:

Написать скрипт который будет бекапить все базы mysql, кроме системных и c помощью утилиты rsync копировать на удаленный сервер.

Скрипт должен проверять все параметры и обрабатывать возможные ошибки. 



```



Ответ на задачу1:

```shell
a)less file.log | cut -d' ' -f1 | uniq -c | sort -nrk 1 | head -n 10 > top_10_ip.txt

b)less file.log | cut -d' ' -f11 | uniq -c | sort -nrk 1 | head -n 10 > top_10_url.txt

c)less file.log | cut -d' ' -f12 | uniq -c | sort -nrk 1 | head -n 10 > top_10_user_agert.txt
```


Ответ на задачу2:

1)
```shell 
http {

    upstream myapp1 {

        server srv1.example.com fail_timeout=1s  max_fails=1;

        server srv2.example.com fail_timeout=1s  max_fails=1;

        server srv3.example.com fail_timeout=1s  max_fails=1;

    }



    server {

        listen 80;



        location / {

            fastcgi_pass http://myapp1;

            proxy_next_upstream error timeout http_502 http_504;

        }

    }

}
```


2)
```shell
http {

    upstream myapp1 {

        server srv1.example.com weight=2 fail_timeout=1s  max_fails=1;  

        server srv2.example.com fail_timeout=1s  max_fails=1;

        server srv3.example.com fail_timeout=1s  max_fails=1;

    }



    server {

        listen 80;



        location / {

            fastcgi_pass http://myapp1;

            proxy_next_upstream error timeout http_502 http_504;

        }

    }

}
```


Ответ на задачу3:

a) Упрощенный конфиг nginx

```

user www-data;

worker_processes auto;

pid /run/nginx.pid;

include /etc/nginx/modules-enabled/*.conf;



events {

        worker_connections 768;

        # multi_accept on;

}



http {



  

        map $remote_addr $var_two {

             default          "0";

            "192.168.10.5"    "1";

        }

        map $http_user_agent $var_three {

            "~ Firefox"   "1";

            "~ Chrome"    "1";

        }

        map "$var_two:$var_three" $var_one {

            "1:1"    "0";

            "0:1"    "1";

            "1:0"    "0";

            "0:0"    "0";

        }







server {
        listen 80 default_server;
        listen [::]:80 default_server;
        access_log /var/log/nginx/phpmyadmin.log combined;
        root /var/www/phpmyadmin;
        index index.html 
        server_name _;

        location / {
        if ($var_one) {
            return 403;
        }
                try_files $uri $uri/ =404;
        }
}
```


b) Упрощенный конфиг nginx

```

user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;
events {
        worker_connections 768;
        # multi_accept on;
}

http {
        map "$http_user_agent" $block {
            "~ Chromium"  "1";
            "~ Firefox"   "1";
            "~ Chrome"    "1";
        }

server {
        listen 80 default_server;
        listen [::]:80 default_server;
        access_log /var/log/nginx/phpmyadmin.log combined;
        root /var/www/phpmyadmin;
        index index.html 
        server_name _;
        location / {

        set $abc "";
        if ($remote_addr != "8.8.8.8"){
        set $abc $block;
        }

        if ($abc) {
            return 403;
        }
                try_files $uri $uri/ =404;
        }
}

```

b) Упрощенный конфиг nginx

Ответ на задачу4:
Берем file1, форматируем его и записываем вывод в file2:
```shell
awk ' BEGIN{FS="\n"; RS=""} {for (i = 1; i <= NF; i+=3) { printf "%s:%s %s\n", $i,$(i+1),$(i+2) }}' file1 > file2
```


Ответ на задачу5:
```shell 
#!/bin/bash
KEY=".ssh/id_rsa"
PORT="22"
ADMIN_EMAIL="email@domain.com"
DESTINATION="alex@192.168.10.5:/home/alex/backup"
MyUSER="root"
MyPASS="gfhjkm"
MyHOST="localhost"
MYSQL="$(which mysql)"
MYSQLDUMP="$(which mysqldump)"
#MYSQL="/usr/local/bin/mysql"
#MYSQLDUMP="/usr/local/bin/mysqldump"
CHOWN="$(which chown)"
CHMOD="$(which chmod)"
GZIP="$(which gzip)"
MBD="$DEST"
HOST="$(hostname)"
DATE="$(date +"%Y%m%d")"
LOG="./backup.log.$DATE"
FILE=""
DBS=""
DIR="./$HOST.$DATE.backup"
# DO NOT BACKUP these databases
IGN="information_schema"
IGN1="performance_schema"
IGN2="mysql"



#Validation check



if  [ -d "$DIR" ]; then
        echo "There is a backup folder on the host. This task is already running or previous run was completed with errors on `hostname`" 
        exit
fi

mkdir $DIR

if  [ -f "$LOG" ]; then
        echo "There is a log file. This task is already running or previous run was completed with errors on `hostname`" 
        exit
fi

touch $LOG
#directing all output to logfile
exec >> $LOG 2>&1



# Get all database list first
DBS="$($MYSQL -u $MyUSER -h $MyHOST -p$MyPASS -Bse 'show databases')"



if [ $? -ne 0 ]; then
        echo "ERROR with connecting to the MySQL! Plese, check." 
        exit
fi



for db in $DBS
do
        if !  { [ "$IGN2" = "$db" ] || [ "$IGN1" = "$db" ] || [ "$IGN" = "$db" ]; }; then 
                FILE="$DIR/$db.$DATE.sql.gz"
                $MYSQLDUMP --opt -u $MyUSER -h $MyHOST -p$MyPASS $db | $GZIP -9 > $FILE
                echo -e "Backup of $db database done">>$LOG
        fi     
 done

        start=$(date +%s)
        rsync -avzh --compress-level=9 ./$DIR -e "ssh -i $KEY -p $PORT" $DESTINATION || (echo -e "Error when rsyncing $domain. \n\n For more information see $LOG:\n\n `tail $LOG`" | mail -s "rsync error" $ADMIN_EMAIL & continue)
        finish=$(date +%s)

        #Delete old logs 
        find ./ -maxdepth 1 -mtime +7 -type f -path "./backup.log.????????" -exec rm -r -f {} \;
        echo -e "`date` *** RSYNC worked for $((finish - start)) seconds">>$LOG

rm -rf ./$DIR
```