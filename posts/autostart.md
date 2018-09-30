Костыль с перезапуском приложение с в cron 
----

```
#!/bin/bash
if pidof 'memcached' > /dev/null 2>&1; then
 echo "Memcached уже запущен" > /dev/null 2>&1
else
 /etc/init.d/memcached start > /dev/null 2>&1
fi
```