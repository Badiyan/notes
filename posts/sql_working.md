Работа с языком SQL 
----

### Работа с базами данных 

```sql
CREATE DATABASE sbase;
-- cоздаем базу данных (дальше не пишу коментарии потому то и так понято) 
DROP DATABASE sbase; 
CREATE DATABASE IF NOT EXISTS sbase; 
CREATE DATABASE sbase collate utf8_general_cli;
SHOW DATABASES;
USE sbase;
```

### Работа с таблицами 

```sql 
CREATE TABLE A
(
   id INT NOT NULL auto_increment, 
   name VARCHAR(30) NOT NULL DEFAULT '',
   cash FLOAT NOT NULL DEFAULT 0,
   PRIMARY KEY (id)
);

DESCRIBE A; --вывести нашу таблицу 
DROP TABLE A;
CREATE TABLE B LIKE A; 
DESCRIBE B; 
DROP TABLE IF EXISTs B;
CREATE TABLE B
	SELECT * FROM A;
CREATE TEMPORARY TABLE C --создать временную саблицу 
	SELECT * FROM A;
DROP TEMPORARY TABLE C;
```
