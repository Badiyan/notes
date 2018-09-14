91.218.214.168





Две ссылки:

https://github.com/hwdsl2/setup-ipsec-vpn#important-notes

https://dimanao.org/l2tp-vpn-server/

================================================    



IPsec VPN server is now ready for use!              



Connect to your new VPN with these details:         



Server IP: 176.36.208.41                            

IPsec PSK: HEYbWYqRqasML9kR                         

Username: vpnuser                                   

Password: DhsbSMxmmSCXYusc                          



Write these down. You'll need them to connect!      



Important notes:   https://git.io/vpnnotes          

Setup VPN clients: https://git.io/vpnclients        



================================================    





vim  /etc/ipsec.conf

```

version 2.0



config setup

  virtual-private=%v4:10.0.0.0/8,%v4:192.168.0.0/16,%v4:172.16.0.0/12,%v4:!192.168.42.0/24,%v4:!192.168.43.0/24

  protostack=netkey

  interfaces=%defaultroute

  uniqueids=no



conn shared

  left=%defaultroute

  leftid=176.36.208.41

  right=%any

  encapsulation=yes

  authby=secret

  pfs=no

  rekey=no

  keyingtries=5

  dpddelay=30

  dpdtimeout=120

  dpdaction=clear

  ike=3des-sha1,3des-sha2,aes-sha1,aes-sha1;modp1024,aes-sha2,aes-sha2;modp1024,aes256-sha2_512

  phase2alg=3des-sha1,3des-sha2,aes-sha1,aes-sha2,aes256-sha2_512

  sha2-truncbug=yes



conn l2tp-psk

  auto=add

  leftprotoport=17/1701

  rightprotoport=17/%any

  type=transport

  phase2=esp

  also=shared



conn xauth-psk

  auto=add

  leftsubnet=0.0.0.0/0

  rightaddresspool=192.168.43.10-192.168.43.250

  modecfgdns="8.8.8.8, 8.8.4.4"

  leftxauthserver=yes

  rightxauthclient=yes

  leftmodecfgserver=yes

  rightmodecfgclient=yes

  modecfgpull=yes

  xauthby=file

  ike-frag=yes

  ikev2=never

  cisco-unity=yes

  also=shared

```



vim /etc/xl2tpd/xl2tpd.conf

```

[global]

port = 1701



[lns default]

ip range = 192.168.42.10-192.168.42.250

local ip = 192.168.42.1

require chap = yes

refuse pap = yes

require authentication = yes

name = l2tpd

pppoptfile = /etc/ppp/options.xl2tpd

length bit = yes

```





vim /etc/ppp/options.xl2tpd

```

+mschap-v2               

ipcp-accept-local        

ipcp-accept-remote       

ms-dns 8.8.8.8           

ms-dns 8.8.4.4           

noccp                    

auth                     

mtu 1280                 

mru 1280                 

proxyarp                 

lcp-echo-failure 4       

lcp-echo-interval 30     

connect-delay 5000       

```

vim /etc/ipsec.secrets

```

%any  %any  : PSK "HEYbWYqRqasML9kR"

```



```

/etc/init.d/ipsec restart && /etc/init.d/xl2tpd restart

```