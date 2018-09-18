# Linux. Загружаемся в Croot из под Life CD Linux

Бывает иногда что Linux машина падает, а данные восстановить нужно. Для этого можно попробовать загрузится через chroot
Для подобных операция лучше всего подойдут специализированнные дистрибутивы например * [system-rescue-cd](http://www.system-rescue-cd.org/)

```
mkdir /mnt/root
mount
fdisk -l
lvs
file -s /dev/sda3
file -s /dev/sda2
file -s /dev/sda4
mount -t ext4 /dev/sda4 /mnt/root/
cd /mnt/root/
ls
ls  -la
df -h
cd ..
umount
umount /mnt/root/
mount -t ext4 /dev/sda3 /mnt/root/
cd root/
ls
mount -o bind /dev dev
mount -o bind /sys sys
mount -o bind /run run
mount -o bind /proc proc
chroot . bin/bash
```

###  Что еще почитать на єту тему?

[http://laurvas.ru/chroot/](http://laurvas.ru/chroot/)
