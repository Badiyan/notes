# GUIDE 

### How to check packets with TCPDUMP

```shell
tcpdump -i wlp2s0 -s 65535 -w  test.pcap
```

### How to check packets with TSHARK

```shell
tshark -i eth0 -f "port  1303"
tshark -i eth0 -f "host 192.168.8.68"
tshark -i eth0 -w capture-output.pcap
tshark -r capture-output.pcap
```

```shell
tshark -n -e frame.number -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e data -T fields >  tshark.log
tshark -i eth1  -n -e frame.time -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e data -T fields -f 'port 3061'
tshark -n -i enp0s8 -e frame.time -e ip.src  -Y "ip.src == 192.168.8.104" -e ip.dst -e tcp.srcport -e tcp.dstport \
-e data  -T fields -f 'dst port 3061'
```

```shell
tshark -nr input.pcap -Y "icmp" -w output.pcap
tshark -nr input.pcap -Y "ip.addr eq 192.168.0.2" -w output.pcap
```

### How to check packets with TESRMSHARK
```shell
termshark -r test.pcap 
```
or
```shell
termshark -r test.pcap | cat
```
