Создадим просто юзера:

```

CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';

FLUSH PRIVILEGES;

```

```

$ mysql -u root -p

Enter password:

```

После успешного подключения, выполним команду создания базы данных:

```

mysql> create database testbase;

```

Затем создадим пользователя baseuser для подключения к базе данных и назначим ему пароль "userpasswd":

```

mysql> grant usage on *.* to baseuser@localhost identified by ‘userpasswd’;

```

И, наконец, назначаем все привилегии (права) на базу testbase пользователю baseuser:

```

mysql> grant all privileges on testbase.* to baseuser@localhost;

```

Символ * (звездочка) означает “все таблицы в базе данных”.



Все, с поставленной задачей мы справились.



Теперь проверим возможность подключения пользователя baseuser к базе данных testbase:

```

$ mysql -u baseuser -p ‘userpasswd’ testbase

```