Средство виртуализации linux LXC





```

lxc-attach --name 129

```



Была замечена вот такая проблема: https://forum.proxmox.com/threads/failed-to-allocate-directory-watch-too-many-open-files.28700/

```

sysctl fs.inotify.max_user_instances=512

```