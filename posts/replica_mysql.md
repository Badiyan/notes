Репликация базы данных Maria DB (Debian)
----

Входные данные:
 - Есть три хоста в одной подсети, MariaDB 10.1, Debian 9.5.
 - ip: 
	192.168.10.239
	192.168.10.240
	192.168.10.246

Создадим меду ними реплику 

### Зачем нужно?
Так удобнее распределять нагрузку на чтение базы данных и осуществлять резервное копирование  

### Репликация MASTER-SLAVE

Выполняю шаги описанные в статье, см. ее [тут](https://ruhighload.com/%D0%9A%D0%B0%D0%BA+%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C+mysql+master-slave+%D1%80%D0%B5%D0%BF%D0%BB%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8E%3F) 

#### Шаг 1. Настройка Мастера

Мастером у нас будет ip 192.168.10.239.  
На сервере, который будет выступать мастером, необходимо внести правки в my.cnf:
```
# выбираем ID сервера, произвольное число, лучше начинать с 1
server-id = 1

# путь к бинарному логу
log_bin = /var/log/mysql/mysql-bin.log

# название Вашей базы данных, которая будет реплицироваться
binlog_do_db = mydatabase

# открываем доступ всем хостам в сети 
bind-address		= 0.0.0.0

```
Перезапускаем Mysql:
```
systemctl restart mysql 
```
#### Шаг 2. Права на репликацию

Далее необходимо создать профиль пользователя, из под которого будет происходить репликация. Для этого запускаем консоль:
```
mysql -u root -p
```
Далее создаем и назначаем права пользователю для реплики:
```
GRANT REPLICATION SLAVE ON *.* TO 'slave_user'@'%' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```
Даем права пользователю slave_user с паролем password

Далее блокируем все таблицы в нашей базе данных:
```
USE newdatabase;
FLUSH TABLES WITH READ LOCK;
```
Проверяем статус Мастер-сервера:
```
SHOW MASTER STATUS;
```
Мы увидим что-то похожее на:
```
MariaDB [(none)]> show master status 
    -> ;
+------------------+----------+--------------+------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+------------------+----------+--------------+------------------+
| mysql-bin.000001 |      747 | mydatabase   |                  |
+------------------+----------+--------------+------------------+
1 row in set (0.00 sec)
```
Выделенные значения мы будем использовать для запуска Слейва

####  Шаг 3. Дамп базы

Теперь необходимо сделать дамп базы данных:
```
mysqldump -u root -p newdatabase > newdatabase.sql
```
Разблокируем таблицы в консоли mysql:
```
UNLOCK TABLES;
```
#### Шаг 4. Создание базы на слейве

В консоли mysql на Слейве создаем базу с таким же именем, как и на Мастере:
```
CREATE DATABASE mydatabase;
```
После этого загружаем дамп (из bash):
```
mysql -u root -p mydatabase < mydatabase.sql
```
#### Шаг 5. Настройка Слейва

В настройках my.cnf на Слейве необходимо указать такие параметры:
```shell 
# ID Слейва, удобно выбирать следующим числом после Мастера
server-id = 2

# Путь к relay логу
relay-log = /var/log/mysql/mysql-relay-bin.log

# Путь к bin логу на Мастере
log_bin = /var/log/mysql/mysql-bin.log

# База данных для репликации
binlog_do_db = newdatabase
```
#### Шаг 6. Запуск Слейва

Нам осталось включить репликацию, для этого необходимо указать параметры подключения к мастеру. В консоли mysql на Слейве необходимо выполнить запрос:
```
CHANGE MASTER TO MASTER_HOST='192.168.10.239', MASTER_USER='slave_user', MASTER_PASSWORD='password',
MASTER_LOG_FILE = 'mysql-bin.000001', MASTER_LOG_POS = 747;
```
# Указанные значения мы берем из настроек Мастера

После этого запускаем репликацию на Слейве:
```
START SLAVE;
```
Статус репликации

Проверить работу репликации на Слейве можно запросом:
```
MariaDB [mydatabase]> SHOW SLAVE STATUS\G
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 192.168.10.239
                  Master_User: slave_user
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000003
          Read_Master_Log_Pos: 583
               Relay_Log_File: mysqld-relay-bin.000005
                Relay_Log_Pos: 871
        Relay_Master_Log_File: mysql-bin.000003
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB: 
          Replicate_Ignore_DB: 
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 0
                   Last_Error: 
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 583
              Relay_Log_Space: 2061
              Until_Condition: None
               Until_Log_File: 
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File: 
           Master_SSL_CA_Path: 
              Master_SSL_Cert: 
            Master_SSL_Cipher: 
               Master_SSL_Key: 
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error: 
               Last_SQL_Errno: 0
               Last_SQL_Error: 
  Replicate_Ignore_Server_Ids: 
             Master_Server_Id: 1
               Master_SSL_Crl: 
           Master_SSL_Crlpath: 
                   Using_Gtid: No
                  Gtid_IO_Pos: 
      Replicate_Do_Domain_Ids: 
  Replicate_Ignore_Domain_Ids: 
                Parallel_Mode: conservative
1 row in set (0.00 sec)

MariaDB [mydatabase]> 
```
Читайте также как настроить Master-Master репликацию на MySQL.

### Читаем по теме: 
[Как настроить мастер мастер репликацию](https://ruhighload.com/%d0%9a%d0%b0%d0%ba+%d0%bd%d0%b0%d1%81%d1%82%d1%80%d0%be%d0%b8%d1%82%d1%8c+mysql+master-master+%d1%80%d0%b5%d0%bf%d0%bb%d0%b8%d0%ba%d0%b0%d1%86%d0%b8%d1%8e%3f)
[Как настроить мастер слейв репликацию](https://ruhighload.com/%D0%9A%D0%B0%D0%BA+%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C+mysql+master-slave+%D1%80%D0%B5%D0%BF%D0%BB%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8E%3F)
[Применение репликации](https://ruhighload.com/%d0%a0%d0%b5%d0%bf%d0%bb%d0%b8%d0%ba%d0%b0%d1%86%d0%b8%d1%8f+%d0%b4%d0%b0%d0%bd%d0%bd%d1%8b%d1%85)
