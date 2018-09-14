Обновление лицензии в Jira.

Обновление лицензии в JIRA, Confluence.



- 1 Смотрим id сервера

- 2 Заходим на my.atlassian.com, Логинимся,

- 3 Копируем ID servera, генерируем новый пароль.





для перезагрузки 

1) /etc/init.d/jira stop

2) подождать  немного, пока процессы остановятся

3) /etc/init.d/jira star

 

ЗАпускаем  конфлюенсе 

/opt/atlassian/confluence/bin/start-confluence.sh



###Ставим задачу в атозагрузку.



```

chkconfig rinetd on

```

###Доступы

```

eleutherius@cms.monpacie.com.ua

eleutherius@jira.monpacie.com.ua

```

Версия дистрибутива:

```

cat /etc/issue

```

 Включаем - выключаем confluence

```

cd /opt/atlassian/confluence/bin

./stop-confluence.sh

./start-confluence.sh

```