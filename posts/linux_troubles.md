# Linux trouble-shooting

Находим и устраняем неисправности Linux

### Получаем инфонрмацию об оперативной памяти

```
cat /proc/meminfo
```
Для фана можем прочитать что там находится:

```
sudo dd if=/dev/mem | cat | strings
```

### Убиаваем процесс
```
ps -A | grep ProgramName
kill 7207
```
Если не помогло - вы пускаем смертельный kill -9
```
kill -9 7207
```

### Информация о процессoре
```
cat /proc/cpuinfo
```
Запускаем top,  смотрим на нагруженность системы, а особенно (ключевой параметр load average)
### Температура процесора
смотрим так:
```
sysctl -a | grep thermal
#или
cat /proc/acpi/thermal_zone/TZS0/temperature
```
или ставим утелиты [https://romantelychko.com/blog/1096/](https://romantelychko.com/blog/1096/)

### USB и PCI устройства
```
lsusb 
lspci
```
