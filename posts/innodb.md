###Восстановление  InnoDB  таблиц  

```

net stop mysql

```

Запуск  в режиме восстановления: 

```

mysqld --console --innodb_force_recovery=6

```

```

> mysqldump --routines -u "user" -p db_name > [path\]db_name.sql

```

```

> mysql -u "user" –p db_name < [path\]db_name.sql

```

 Смотри также: https://habr.com/post/125358/



Включаем  базу в режиме восстановления 

```

[mysqld]

innodb_force_recovery = 1

```