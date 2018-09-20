Смотрим iptables 

```

iptables -L -n

```

Рабочий конфиг 

```

source /etc/network/interfaces.d/*



auto lo

iface lo inet loopback

iface lo inet6 loopback



auto enp0s31f6

iface enp0s31f6 inet static

  address 138.201.131.133

  netmask 255.255.255.192

  gateway 138.201.131.129

  # route 138.201.131.128/26 via 138.201.131.129

  up route add -net 138.201.131.128 netmask 255.255.255.192 gw 138.201.131.129 dev enp0s31f6



iface enp0s31f6 inet6 static

  address 2a01:4f8:172:2ec4::2

  netmask 64

  gateway fe80::1



auto vmbr0

iface vmbr0 inet static

    address 138.201.131.133

    netmask 255.255.255.255

    bridge_ports none

    bridge_stp off

    bridge_fd 0

    bridge_maxwait 0

    pre-up brctl addbr vmbr0

    up ip route add 138.201.45.145/32 dev vmbr0

    





auto vmbr1

iface vmbr1 inet static

    address 10.10.10.1

    netmask 255.255.255.0

    bridge_ports none

    bridge_stp off

    bridge_fd 0



    post-uo /sbin/iptables -t nat -I PREROUTING --dst138.201.131.133-p tcp --dport 1122 -j DNAT --to-destination 10.10.10.11:22

    post-up echo 1> /proc/sys/net/ipv4/ip_forward

    post-up   iptables -t nat -A POSTROUTING -s '10.10.10.0/24' -o enp0s31f6 -j MASQUERADE

    post-down iptables -t nat -D POSTROUTING -s '10.10.10.0/24' -o enp0s31f6 -j MASQUERADE



```


* [Читаем эту статью ](http://www.rhd.ru/docs/manuals/enterprise/RHEL-4-Manual/security-guide/s1-firewall-ipt-fwd.html)  

Скрипт от одного нашего клиента.Тебе стопудняк пригодится

```

#!/usr/bin/env bash



IPTABLES='/sbin/iptables'

 

$IPTABLES -F

$IPTABLES -t nat -F

$IPTABLES -t mangle -F

$IPTABLES -X

$IPTABLES -t nat -X

$IPTABLES -t mangle -X



### NetForce made it ###



#Добавляем возможность NAT-ить в ядро LINUX 

echo 1 > /proc/sys/net/ipv4/ip_forward



iptables -A FORWARD -i vmbr0 -j ACCEPT

iptables -A FORWARD -o vmbr0 -j ACCEPT



#Включаем маршрутизацию между сетями 

iptables -t nat -A POSTROUTING -o vmbr0 -j MASQUERADE



# Пробрасываем порты на внутренний хост



iptables -t nat -A PREROUTING -i vmbr0 -p tcp --dport 2230 -j DNAT --to 192.168.3.30:22

iptables -A FORWARD -i vmbr0 -p tcp --dport 2230 -d 192.168.3.30 -j ACCEPT







#/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 6379 -j DNAT --to-destination 192.168.3.10:6379

####



##############IPtables rules redirecting#################

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 2111 -j DNAT --to-destination 192.168.3.8:22

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 32222 -j DNAT --to-destination 192.168.3.22:22





# FTP domotronika

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 37121 -j DNAT --to-destination 192.168.3.71:21

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 11071:11171 -j DNAT --to-destination 192.168.3.71

#FTP digitov.secl.ua

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 37221 -j DNAT --to-destination 192.168.3.72:21

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 10072:10172 -j DNAT --to-destination 192.168.3.72

#FTP nodelearning

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 37321 -j DNAT --to-destination 192.168.3.73:21

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 12073:12173 -j DNAT --to-destination 192.168.3.73

#FTP makewear.secl.com.ua

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 37421 -j DNAT --to-destination 192.168.3.74:21

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 13073:13173 -j DNAT --to-destination 192.168.3.74

#FTP alifmarket.secl.com.ua

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 38221 -j DNAT --to-destination 192.168.3.82:21

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 14082:14182 -j DNAT --to-destination 192.168.3.82

#FTP skidka.ll

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 38121 -j DNAT --to-destination 192.168.3.81:21

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 15081:15181 -j DNAT --to-destination 192.168.3.81







#Review forward

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 2109 -j DNAT --to-destination 192.168.3.76:81



#Skidka ports forward

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 7700 -j DNAT --to-destination 192.168.3.81:7700 

/sbin/iptables -t nat -I POSTROUTING -p tcp -s 192.168.3.81 --sport 7700 -j SNAT --to-source 192.168.3.2:7700

/sbin/iptables -t nat -I PREROUTING --dst 178.210.129.129 -p tcp --dport 7700 -j DNAT --to-destination 192.168.3.81:7700

/sbin/iptables -t nat -I POSTROUTING -p tcp -s 192.168.3.81 --sport 7700 -j SNAT --to-source 178.210.129.129:7700


#VM CT169 ports forward

/sbin/iptables -t nat -I PREROUTING --dst 192.168.3.2 -p tcp --dport 12321 -j DNAT --to-destination 192.168.3.92:12321

/sbin/iptables -t nat -I POSTROUTING -p tcp -s 192.168.3.92 --sport 12321 -j SNAT --to-source 192.168.3.2:12321

/sbin/iptables -t nat -I PREROUTING --dst 178.210.129.129 -p tcp --dport 12321 -j DNAT --to-destination 192.168.3.92:12321

/sbin/iptables -t nat -I POSTROUTING -p tcp -s 192.168.3.92 --sport 12321 -j SNAT --to-source 178.210.129.129:12321


# Разрешаем доступ клиентам 

/sbin/iptables -I INPUT -p tcp --dport 22 -s 82.144.210.22 -j ACCEPT # NetForce

/sbin/iptables -I INPUT -p tcp --dport 22 -s 195.69.86.80/28 -j ACCEPT # NetForce

/sbin/iptables -I INPUT -p tcp --dport 22 -s 37.57.125.202 -j ACCEPT # NetForce

/sbin/iptables -I INPUT -p tcp --dport 22 -s 77.123.137.176/28 -j ACCEPT # NetForce

#/sbin/iptables -A INPUT -p tcp --dport 22 -j DROP


# Enable Moscow VPN for 192.168.3.129 - 192.168.3.158:

#/sbin/iptables -t nat -A POSTROUTING -s 192.168.3.128/27 ! -d 192.168.3.128/27 -o tun0 -j SNAT --to-source 10.8.0.6

#/sbin/ip r a 217.23.138.116 via 192.168.3.1 dev vmbr0 t vpn 

#/sbin/ip r a 192.168.3.0/24 dev vmbr0  proto kernel  scope link  src 192.168.3.2 t vpn 

#/sbin/ip r a default via 10.8.0.5 dev tun0 t vpn

#/sbin/ip ru a from 192.168.3.128/27 lookup vpn

exit 0

```