 Ставим эту штуку

```
sudo apt-get install apache2-utils
``` 

 Потом создаем пароль

```
sudo htpasswd -c /etc/nginx/.htpasswd exampleuser
```

 Добавляем строчки :

```
    auth_basic "Please, enter login and password";
    auth_basic_user_file    "/var/www/alex/.htpasswd";
```



Пример конфигурации nginx 

```

 server {
  listen       portnumber;
  server_name  ip_address;
  location / {
      root   /var/www/mywebsite.com;
      index  index.html index.htm;
      auth_basic "Restricted";                                #For Basic Auth
      auth_basic_user_file /etc/nginx/.htpasswd;  #For Basic Auth
  }
}

```

 Перезагружаем сервер 



```
/etc/init.d/nginx reload 
```
