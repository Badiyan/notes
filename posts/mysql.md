###Меняем пароль root 

Если после установки MySQL ни разу не вводился пароль суперпользователя, то для входа не требуется вводить пароль, следовательно срочно задаем пароль, делается это через команду mysqladmin :
```
$ mysqladmin -u root password NEWPASSWORD
```
где NEWPASSWORD - это пароль 

Например :
```
$ mysqladmin -u root password kkdfDS3lKD
```
Если пароль уже задан, то изменить его можно следующим образом :
```
$ mysqladmin -u root -p 'oldpassword' password newpassword
```
 где oldpassword - старый пароль
newpassword - новый пароль
Например
```
$ mysqladmin -u root -p '123456' password 'D2Mellj1'
```
 Для изменения пароля другого пользователя, не root, выполняем следующую команду
```
$ mysqladmin -u username -p oldpassword password newpassword
```
где username - имя пользователя
oldpassword - старый пароль
newpassword - новый пароль
####Так же существует второй способ задания и изменения паролей - использование команд MySQL.
MySQL хранит имя пользователя и пароли в таблице пользователей в базе данных MySQL. Можно непосредственно в таблице базы данных обновить пароль, используя этот метод, для пользователя user_name например так:

1) Войти на сервер MySQL, ввести следующую команду в командной строке:
```$ mysql -u root -p```

2) Переходим в базу данных mysql:

```mysql> use mysql;```

3) Изменить пароль для пользователя user_name, для этого вводим команду:

```
mysql> update user set password=PASSWORD("NEWPASSWORD") where User='user_name';
```
где user_name - имя пользователя
newpassword - новый пароль, т.е. знать старый пароль не нужно, если он был задан. Часто используют эту команду, когда забывают пароли.
4) Обязательно, перезагрузка привилегий:
```
mysql> flush privileges;
mysql> quit
```
