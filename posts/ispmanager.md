Смотрим логи 

```
/usr/sbin/logrotate -d -f <path_to_config_of_required_web_domain>
```



```
tail -f /usr/local/mgr5/var/ispmgr.log
```

перезагружаем 

```
/usr/local/mgr5/sbin/mgrctl -m ispmgr exit
```

Смотрим актуальную версию 

```
/usr/local/mgr5/bin/core -V
/usr/local/mgr5/bin/core ispmgr -V
```

обновляем лицензию на пробный триал



```
delete the license file from the server: rm /usr/local/mgr5/etc/ispmgr.lic   
download the file: /usr/local/mgr5/sbin/licctl fetch ispmgr   
open the control panel web-interface https://:1500/ispmgr   
```