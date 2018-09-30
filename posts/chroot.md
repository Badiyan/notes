Linux. Загружаемся в Croot из под Life CD Linux
----

Бывает иногда что Linux машина падает, а данные восстановить нужно. Для этого можно попробовать загрузится через chroot
Для подобных операция лучше всего подойдут специализированнные дистрибутивы например * [system-rescue-cd](http://www.system-rescue-cd.org/)

```
mkdir /mnt/root
mount
fdisk -l
# смотрим где находится наш диск с корнефой фс
file -s /dev/sda3
mount -t ext4 /dev/sda4 /mnt/root/
cd /mnt/root/
mount -t ext4 /dev/sda3 /mnt/root/

mount -o bind /dev dev
mount -o bind /sys sys
mount -o bind /run run
mount -o bind /proc proc
chroot . bin/bash
```

###  Что еще почитать на эту тему?

[http://laurvas.ru/chroot/](http://laurvas.ru/chroot/)
