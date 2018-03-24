Ниже приведены кусочки кода, возможно пригодится
### Q-in-Q


`Switch_config#dot1q-tunnel` - включаем глобально Q-in-Q
Настраиваем порт:
```python
Switch_config_g0/1#switchport mode ?
  access                    -- Access mode
  trunk                     -- Trunk mode
  dot1q-translating-tunnel  -- Dot1q translating tunnel mode
  dot1q-tunnel-uplink       -- Dot1q tunnel uplink mode
```
Представим, что наш порт даунлинк, он принимает трафик у абонентов
```python
Switch_config_g0/1#switchport mode dot1q-translating-tunnel
```
на аплинковом нужно было аплик режим включить совершенно верно
Настраивайте через консоль.
Он после настройки в глобальном конфиге он начинает оборачивать все вланы во влан pvid его портов
Чтобы он не навешивал второй влан нужно - выполнить команду:
```python
Switch_config_g0/1# dot1q-translating-tunnel mode flat translate 1to1 10-15 40 ?
  <0-7>    -- new 802.1Q priority value
  <cr>
Switch_config_g0/1# dot1q-translating-tunnel mode flat translate 1to1 10-15 40
```
Тоесть он транслирует 10-15 вланы в влан 40
Чтобы завернуть необходимые вланы в Q-in-Q необходимо:
```python
Switch_config_g0/1# dot1q-translating-tunnel mode qinQ translate 10-15  10
```
тоесть  10 -15 влан оборачиваються в 10 влан

Настроим плоскую передачу тегов в :
```python
interface GigaEthernet0/1
 switchport mode dot1q-tunnel-uplink
 switchport dot1q-translating-tunnel mode flat translate 1to1 10 10 0
!
interface GigaEthernet0/2
 switchport mode dot1q-translating-tunnel
 switchport dot1q-translating-tunnel mode flat translate 1to1 10 100 0
 switchport dot1q-translating-tunnel mode flat translate 1to1 100 10 0
!
interface GigaEthernet0/3
Ethernet0/13
!
dot1q-tunnel
vlan 1,10,100
!

```



### ACL
```python
!
! ### Нафиг нетбиос и dhcp-серверы со стороны клиентов
ip access-list extended subs.filter
deny tcp any any eq 135
deny tcp any any eq 136
deny tcp any any eq 137
deny tcp any any eq 138
deny tcp any any eq 445
deny udp any any eq 68
permit ip any any
!
! ### По умолчанию разрешим людям получать адреса по DHCP
ip access-list extended sub-DUMMY
permit udp any eq 68 any eq 67
deny ip any any
!
interface GigaEthernet0/1
 ip access-group subs.filter
!

```


### Loopback detect

На порту выполнить такую команду:
Current configuration:
```python
!
interface GigaEthernet0/23
 keepalive 15
Switch_config#
```
Выключает порт при петле

```python
Switch_config#error-disable-recovery ?
  <0-2147483647[5]> - recovery period(unit:seconds)
```
Восстанавливает порт.

### MULTICAST
Для проверки Multicast используем два ПК. Один их них (VLC Streamer) подключим к GE 0/5 порту OLT-а, другой (VLC клиент) подключим к UNI порту ONU. Мультикаст будет  транслироваться в 1000-ом VLAN_е.

Сделаем следующую настройку на BDCOM P3310B:
```python
interface GigaEthernet0/5
 switchport trunk vlan-untagged none
 switchport mode trunk
 switchport pvid 1000

interface EPON0/1
...
 switchport mode trunk
 switchport protected

interface EPON0/1:13
 onu-configuration
  epon onu port 1 ctc vlan mode tag 200
  epon onu port 1 ctc mcst tag-stripe enable
  epon onu port 1 ctc mcst mc-vlan add 1000

ip mcst enable
ip mcst querier enable
ip mcst mrouter interface GigaEthernet0/5
ip mcst mc-vlan 1000 range 239.255.12.1
```

В итоге мы получили положительный результат, ONU прошла тест.

### Динамический конфиг

```python
epon onu-config-template a
 cmd-sequence 1 epon onu port 1 ctc rate-limit %1 ingress
 cmd-sequence 2 epon onu port 1 ctc vlan mode tag %2
 cmd-sequence 3 epon onu ip address static %3 255.255.255.0 gateway 10.1.1.1 vlan 1
 cmd-sequence 4 epon onu all-port ctc flow-control
!
!
interface Null0
!
interface FastEthernet5/1
 no ip address
 no ip directed-broadcast
!
interface PSG0/1
 epon psg member active EPON1/1
 epon psg member standby EPON9/1
 epon pre-config-template a binded-onu-llid 2 param 20000 102 10.1.1.2
 epon pre-config-template a binded-onu-llid 1 param 50000 101 10.1.1.1
 epon bind-onu mac fcfa.f718.adfc 1
 epon bind-onu mac fcfa.f709.1111 2
 epon bind-onu mac fcfa.f712.4185 3
 switchport mode trunk
 switchport protected 1
!
interface PSG0/1:1
  epon onu port 1 ctc vlan mode tag 101
  epon onu port 1 ctc flow-control
  epon onu port 1 ctc rate-limit 50000 ingress CBS 10000 EBS 0
  epon onu port 2 ctc flow-control
  epon onu port 3 ctc flow-control
  epon onu port 4 ctc flow-control
  epon onu ip address static 10.1.1.1 255.255.255.0 gateway 10.1.1.1 vlan 1
!
interface PSG0/1:2
  epon onu port 1 ctc vlan mode tag 102
  epon onu port 1 ctc flow-control
  epon onu port 1 ctc rate-limit 20000 ingress CBS 10000 EBS 0
  epon onu port 2 ctc flow-control
  epon onu port 3 ctc flow-control
  epon onu port 4 ctc flow-control
  epon onu ip address static 10.1.1.2 255.255.255.0 gateway 10.1.1.1 vlan 1
!
interface PSG0/1:3
  epon onu port 1 ctc vlan mode tag 2000
  epon onu port 2 ctc vlan mode tag 2000
  epon onu port 3 ctc vlan mode tag 2000
  epon onu port 4 ctc vlan mode tag 2000
  epon onu port 1 ctc mcst tag-stripe enable
  epon onu port 1 ctc mcst mc-vlan add 4001
  epon onu port 2 ctc mcst tag-stripe enable
  epon onu port 2 ctc mcst mc-vlan add 4001
  epon onu port 3 ctc mcst tag-stripe enable
  epon onu port 3 ctc mcst mc-vlan add 4001
  epon onu port 4 ctc mcst tag-stripe enable
  epon onu port 4 ctc mcst mc-vlan add 4001

```



### LACP

```python
interface gigaEthernet 0/1
switchport trunk vlan-allowed 5,983
switchport mode trunk
aggregator-group 1 mode lacp


interface g0/2
switchport trunk vlan-allowed 5,983
switchport mode trunk
aggregator-group 1 mode lacp
```
