### Увеличиваем обьем загружаемого файла PHP

You need to set the value of upload_max_filesize and post_max_size in your php.ini :

```

; Maximum allowed size for uploaded files.

upload_max_filesize = 40M



; Must be greater than or equal to upload_max_filesize

post_max_size = 40M



memory_limit = 32M;



```

After modifying php.ini file(s), you need to restart your HTTP server to use new configuration.



If you can't change your php.ini, you're out of luck. You cannot change these values at run-time; uploads of file larger than the value specified in php.ini will have failed by the time execution reaches your call to ini_set.
