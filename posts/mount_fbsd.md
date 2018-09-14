The same way you can format any other disk.



I usually format my USB sticks by creating a single da0s1 slice and then

one (or more) BSD labels in that slice, by typing the commands:

```

        fdisk -BI /dev/da0

        bsdlabel -w -B /dev/da0s1

        newfs /dev/da0s1a

```

If they are going to be used by non-BSD systems, I prefer msdosfs, so I

use:

```

        fdisk -BI /dev/da0

        newfs_msdos /dev/da0s1

```

The command-line options and what they do will be more obvious if you

read the manpages of fdisk(8), bsdlabel(8), newfs(8), and newfs_msdos(8).









### Mounting NTFS on FreeBSD



This post helped me figure all this out.



I need to access a USB hard drive in NTFS on FreeBSD. In order to mount NTFS partitions, FreeBSD uses ntfs-3g FUSE module.



First, make sure the fuse kernel module is loaded. This can be done adhoc with kldload fuse. But to have it loaded at boot time, add the following line in /boot/loader.conf:

```

fuse_load="YES"

```

Then, install fusefs-ntfs package:



```

pkg install fusefs-ntfs

```

Now the OS supports NTFS, you can plugin the device. Use dmesg to figure out the device ID (d0):



```

da0 at umass-sim0 bus 0 scbus4 target 0 lun 0

da0: <WD Ext HDD 1021 2021> Fixed Direct Access SPC-2 SCSI device

da0: Serial Number 574D415A4135333836313839

da0: 40.000MB/s transfers

da0: 1907727MB (3907024896 512 byte sectors)

da0: quirks=0x2<NO_6_BYTE>

```

Use gpart to show its partitions:



```

> ~ gpart show /dev/da0

=>        63  3907024833  da0  MBR  (1.8T)

          63        1985       - free -  (993K)

        2048  3907022848    1  ntfs  (1.8T)

```

You can also find the device node for the partition under /dev:

```

➜  ~ ls -l /dev/da0*

crw-r-----  1 root  operator  0x72 Feb  3 12:07 /dev/da0

crw-r-----  1 root  operator  0x73 Feb  3 12:07 /dev/da0s1

```

Now we are ready to mount it:



```

ntfs-3g /dev/da0s1 /mnt -o ro

```

-o ro makes sure it's mounted read-only. You can remove it to mount it read-write.



Note that I tried to use mount hoping there is a consolidated command for mounting different kinds of file systems. But it wasn't successful:



```

➜  ~ mount -t ntfs-3g /dev/da0s1 /mnt

mount: /dev/da0s1: Operation not supported by device



➜  ~ mount -t ntfs /dev/da0s1 /mnt

mount: /dev/da0s1: Operation not supported by device

```

Also note that usually mounting a partition can only be done by root, or using sudo, which result in the mounted path is owned by root:wheel. However you can mount the partition as a specified user and group using uid and gid options.



First, find out the user and group IDs of the preferred user:



### id john

uid=1001(john) gid=1001(john) groups=1001(john),0(wheel)



Now run following command to mount:

```

ntfs-3g /dev/da0s1 /mnt -o ro,uid=1001,gid=1001



Now /mnt is owned by john:john.
