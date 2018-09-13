# Мои заметки по настройке OLT/ONU BDCOM

[Рекомендации по конфигам](CONFIG.md "Рекомендации по конфигам")/
[Пример настройки P3310B](P3310B.md "Пример настройки P3310B")/
[Пример настройки P3616](P3616.md "Пример настройки P3616")


##  Тестирование ONU

### 1.	Подключение и регистрация
(Подключаем подключаем максимальное количество рзличных онушек к  одному порту и смотрим как проходит регистрация)
```python
Switch_config#logging buffered ?
  <4096-2147483647>  -- Logging buffer size(bytes)
  alerts             -- Immediate action needed
  critical           -- Critical conditions
  debugging          -- Debugging messages
  emergencies        -- System is unusable
  errors             -- Error conditions
  informational      -- Informational messages
  notifications      -- Normal but significant conditions
  rate-limit         -- Set rate-limit
  warnings           -- Warning conditions
  time-range         -- Set the time range for logging
```

При регистрации онушек сравнить процес регистрации.
### 2.	Проверяем DDM и базовую информацию.
```python
#show epon optical-transceiver-diagnosis interface epON 0/1:1
# show epon inf  epon 0/1:1 onu ctc basic_info
# show epon onu informatoin
```
Смотрим ошибки на порту:
```python
#show int GigabitEternet 0/1
```
### 3.  DBA/SBA
3.	Включим на OLT инструмент DBA.
DBA – динамическое расспередиление скорости,
SBA - статической распределение скорости.

```python
Switch_config# epon dba hardware cycletime 2500 discovery-freqence 64 discovery-length 1024
```

После этого необходимо повторить пунут 1.
4.	Пропинговать какой-то сайт с DBA и без DBA. Прогнать онушку с помошю iperf с алгоритмом DBA и без. Не забыть увеличить SLA  до 1G

### 4. Management IP ADDRES

У  ONU есть дава IP адреса:
- Out-band – тот который виден с UNI порта( Ethernet ). 192.168.1.1 для онушки Fora.
- IN-band – тот который видно с OLT.

На Out-band со вне не достучатся. Необходимо:
- узнат какой внешний айпишник;
- зайти на WEB интерфейс;
- зайти в Telnet, посмотркть возможно ли его прошивать через Telnet.

IN-band по умолчанию не существует. Есть две команды для его назначения:

```python
Switch_conf_epon0/1:1# epon onu ip address static 192.168.1.216  255.255.255.0 gatewey 192.168.1.20  vlan 200
```

Есть уще команда OAM:
```python
 Switch_conf_epon0/1:1#epon onu ctc ip address static 192.168.1.216 255.255.255.0 gatewey 192.168.1.20 cvlan 200 svlan 0 priority 5
```
Необходимо проверить:
-  выполняется ли команда;
- посмотреть пингуется ли онушка 200 влане.
- проверить ли в разных вланах пингуется ли онушка.
- проверить  ест ли доступ к Telnet and WEB через внутренний айпишник.

###  5. Перепрошивка  ONU через OLT.
```python
Switch#epon update onu image image.dat int epON 0/1:1
```

И обязательно нужно закомитить после перезагрузки.

```python
Switch#epon commit-onu-image-update interface epON 0/1:1
```


### 6. Storm control
```python
Switch_config_epon0/1:6#epon onu all-port storm-control mode ?
1                       -- limit broadcast
2                       -- limit multicast
3                       -- limit unkown unicast
4                       -- limit all packet
Switch_config_epon0/1:6#epon onu all-port storm-control mode 4 threshold 256
```

### 7. ОБНАРУЖЕНИЕ ПЕТЕЛЬ (не кольца!!!)
Loop back detect (LBD)
Для LBD tpid (номер протокола) заголовок FFFA.
Пример теста:
- включимся снифером в сеть с необходимым фильтром
Eth.type == 0XFFFA
Или настроить фильтр по маку онушки.
Если на онушки эта обция включина по умолчанию и не выключается то все норм .

```python
Switch conf_epon 0/1:1#epon onu all port lopback detect
Switch conf_epon 0/1:1#epon onu ctc all port lopback detect
```

### 8. Тестируем пропускную способность онушки. В полном дублексе и полудуплексе на пол часаю (делем с DBA )


### 9. Применение шаблонов
Делаем шаблон под ONU на 10 -15  строчек хотя бы, смотрим как поведет себя ОНУ.


### 10. Проверка опции 82.
Онушка не должна слать опцию 82 по умолчанию.
Используем для этого программу DHCDROP – отправляем и сравниваем DHCP пакеты.
Включаем опцию и смотрим работает она или нет на ONU:
Switch_epon 0/1:1#epon onu dhcp snooping opt 82 enable opend – end – forward default
-	Remoute id – обяательно должен иметь мак онушки.
На OLT:

```python
ip dhcp-relay snooping
ip dhcp-relay snooping vlan  109-112
ip dhcp-relay snooping information option format hn-type host
```
### 11. Multicast Vlan (iptv)
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

### 12. Port Secyrity (безопасность порта) – ограничивает таблицу мак адресов онушки.
```python
Switch_config_epon 0/1:1# switchpotr port security mоde dinamic
Switch_config_epon 0/1:1# switchport Port-security dynamic maximum 5
```
Для проверки используем DHCPdrop (в DHCPdrop генерируем линейку мак адресов).

initial MAC address - задаёт MAC адрес источника используемый при отправке первого DHCP сообщения, либо используемый постоянно, в случае использования опции -f (flood) вместе с опцией -r. Если не указан, то используется случайный MAC адрес источника.



### 13. Проверка MTU.
A) Создаем на коммутаторе QinQ трафик. (На через один коммутатор пропускаем 1 vlan, через другой навешиваем еще один  vlan в QinQ )
Б) Пропускаем трафик скозь онушку.
Или же пользуемся для этого [scapy](https://scapy.readthedocs.io/en/latest/ "scapy")
### 14. Проверим режимы работы медного порта
`Switch_ conf_ epon 0/1:1 # epon onu all-port ctc vlan mod tag` – аналог режима assecc для коммутаторов.
 Translation – пересылка влана.
Transparend – самый простой режим и по умолчанию онушка находится в нем. (ничего не делает с трафиком)
Vlan-staking – QinQ.
Aggregation – если от одного пер.
Протестировать при режимах:
1) Trunc
2) Tag
3) Transparend
### 15. Шторм контроль (smart control) – ограничиваем броткасный и мультикасный флуд
```python
# epon onu all port shtormcontrol mode 4 thetiod 256
```
Этот трафик идет от медного порта в сторону олта, если трафика больше онушка болкирует пакеты.


### Справочник терминов
**Dynamic bandwidth allocation (или DBA)** – динамическое распределение полосы пропускания.
Метод динамического увеличения или уменьшения полосы пропускания в реальном времени, чтобы обеспечить загрузку линии (канала) с максимальной эффективностью. B ISDN при одновременной передаче данных и речи средства DBA работают с протоколом MPPP и дают пользователю возможность принять данные по одной из линий, даже если обе линии заняты передачей данных.
**MPPP (Multilink Point-to-Point Protocol)** - многоканальный протокол "точка-точка".
DBA бывает:
1. NSR (None status report)
2. SR (Status report – используется современными OLT-ами)
TQ  (Time Quant) – квант времени.

Основные параметры DBA которые можно настраивать на OLT-а:
1) Cicle time [TQ]
2) Discovery-length [TQ]
3) Discovery-frequency
4) Dynamic cicle-time

**Service Level Agreement** – SLA (Соглашение об уровне предоставления услуги)
Service Level Agreement или SLA (соглашение об уровне сервиса) – три слова, определяющие подходы компании к организации ИТ-процессов. Согласно ITIL (IT Infrastructure Library) SLA – это мини-договор, устанавливающий параметры качества предоставляемых бизнесу ИТ-услуг.

**GARP VLAN Registration Protocol (GVRP)** — сетевой протокол канального уровня модели OSI/ISO, позволяющий устройству локальной сети сообщить соседним устройствам, что оно желает принять пакеты для одной или нескольких VLAN. Главная цель GVRP — позволить коммутаторам автоматически обнаружить информацию о VLAN, которая иначе должна была бы быть вручную сконфигурирована в каждом коммутаторе. Этого можно достичь использованием GVRP — распространить идентификаторы VLAN по локальной сети. GVRP также может быть использован сетевыми серверами. Эти серверы обычно конфигурируются для вхождения в несколько VLAN, и затем сообщают коммутаторам о VLAN, к которым они хотят присоединиться.
GVRP протокол описан в стандарте IEEE 802.1p.

**DHCP snooping**
DHCP snooping — функция коммутатора, предназначенная для защиты от атак с использованием протокола DHCP. Например, атаки с подменой DHCP-сервера в сети или атаки DHCP starvation, которая заставляет DHCP-сервер выдать все существующие на сервере адреса злоумышленнику.
DHCP snooping регулирует только сообщения DHCP и не может повлиять напрямую на трафик пользователей или другие протоколы. Некоторые функции коммутаторов, не имеющие непосредственного отношения к DHCP, могут выполнять проверки на основании таблицы привязок DHCP snooping (DHCP snooping binding database). В их числе:
**Dynamic ARP Protection (Inspection)** — проверка ARP-пакетов, направленная на борьбу с ARP-spoofing,
IP Source Guard — выполняет проверку IP-адреса отправителя в IP-пакетах, предназначенная для борьбы с IP-spoofingом.
