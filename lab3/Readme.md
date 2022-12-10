Комментарии и описание ниже в Readme, конфиги всех устройств в папке configs, сама выгруженная лаба - файл homework3.unl

**Топология**

<img width="412" alt="Screenshot 2022-12-10 at 23 26 30" src="https://user-images.githubusercontent.com/89082482/206874032-737296eb-1715-49ec-825e-ecbbde2d6435.png">

**Настройки на устройствах:**

VPC1:

```
ip dhcp
save
```

VPC2:

```
ip dhcp
save
```

Switch3, Switch4, Switch5:

```
так же, как в lab1
```

Router1:

```
<Все команды из lab1>

#configure dhcp
enable
configure terminal

#exclude addresses
ip dhcp excluded-address 10.0.10.1 10.0.10.10
ip dhcp excluded-address 10.0.20.1 10.0.20.10

ip dhcp pool vlan10
network 10.0.10.0 255.255.255.0
dns-server 8.8.8.8
default-router 10.0.10.1
exit

ip dhcp pool vlan20
network 10.0.20.0 255.255.255.0
dns-server 8.8.8.8
default-router 10.0.20.1
exit

#configure nat

ip nat pool HwPool 100.0.1.10 100.0.1.40 netmask 255.255.255.0
access-list 1 permit 10.0.10.0 0.0.0.255
access-list 1 permit 10.0.20.0 0.0.0.255
ip nat inside source list 1 pool HwPool

interface e0/0
ip nat inside

interface e0/0.1
ip nat inside

interface e0/0.2
ip nat inside
exit

interface e0/1
no shutdown
ip address 100.0.1.1 255.255.255.0
ip nat outside

exit
exit
wr
```

Router2:

```
enable
configure terminal

interface e0/0
no shutdown
ip address 100.0.1.254 255.255.255.0

exit
exit
wr
```

**Выводы с устройств**

Информация с Router1 о выданных Ip-адресах, он действительно выдал адрес каждому VPC. Первые 10 были исключены, поэтому выдан одиннадцатый
<img width="995" alt="Screenshot 2022-12-10 at 23 53 48" src="https://user-images.githubusercontent.com/89082482/206874853-10cb24bc-1a9b-44e5-96de-648377bb2ba6.png">

ping с VPC1 на Router2, прошел успешно
<img width="995" alt="Screenshot 2022-12-11 at 00 08 01" src="https://user-images.githubusercontent.com/89082482/206875320-904975da-3944-4748-8e39-9fa68d8e82b2.png">

ping с VPC2 на Router2, прошел успешно
<img width="995" alt="Screenshot 2022-12-11 at 00 10 15" src="https://user-images.githubusercontent.com/89082482/206875375-c3f631da-324e-44a3-9815-55df7bf68b05.png">

Информация о переведенных с помощью nat адресах на Router1, ping-и прошли через nat
<img width="995" alt="Screenshot 2022-12-11 at 00 10 56" src="https://user-images.githubusercontent.com/89082482/206875398-aa1ac99a-4de6-414c-95e8-06491fb88f1a.png">

