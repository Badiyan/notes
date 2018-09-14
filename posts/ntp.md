```ln -sf /usr/share/zoneinfo/Europe/Kiev /etc/localtime```

Далее настраиваем синхронизацию :



установим

```apt-get install ntpdate```



запустим ( пример )

```ntpdate -bs pool.ntp.org```

 

Добавим запись в cron