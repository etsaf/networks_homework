Комментарии и описание ниже в Readme, конфиги всех устройств в папке configs, сама выгруженная лаба - файл homework1.unl

**Топология**

<img width="603" alt="Screenshot 2022-12-09 at 20 59 08" src="https://user-images.githubusercontent.com/89082482/206764140-8fe76cb1-860b-46c0-9134-ecb305f780cb.png">

**Настройки на устройствах**

VPC1:

```
ip 10.0.10.2 255.255.255.0 10.0.10.1
save
```


VPC2:

```
ip 10.0.20.2 255.255.255.0 10.0.20.1
save
```

Switch3:

```
#create vlans
enable
configure terminal
vlan 10
exit
vlan 20
exit

#configure interfaces
interface e0/0  #к PC1
switch mode access
switch access vlan 10
exit

interface e0/2  #к Switch4
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

interface e0/1  #к Switch5
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

vtp mode transparent
exit
wr
```

Switch4:

```
#create vlans
enable
configure terminal
vlan 10
exit
vlan 20
exit

#configure interfaces
interface e0/0  #к PC2
switch mode access
switch access vlan 20
exit

interface e0/2  #к Switch3
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

interface e0/1  #к Switch5
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

vtp mode transparent
exit
wr
```

Switch5:

```
#create vlans
enable
configure terminal
vlan 10
exit
vlan 20
exit

#configure interfaces

interface e0/0 #к Switch3
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

interface e0/1 #к Switch4
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

interface e0/2 #к Router
switchport trunk allowed vlan 10,20
switchport trunk encapsulation dot1q
switchport mode trunk
exit

spanning-tree vlan 1 root primary
spanning-tree vlan 10 root primary
spanning-tree vlan 20 root primary

vtp mode transparent
exit
wr
```

Router:

```
enable
configure terminal

interface e0/0
no shutdown

interface e0/0.1
encapsulation dot1Q 10
ip address 10.0.10.1 255.255.255.0

interface e0/0.2
encapsulation dot1Q 20
ip address 10.0.20.1 255.255.255.0

exit
exit
wr
```



**Выводы с устройств:**
__________

Ping VPC1 с VPC2 и наоборот проходит:

На VPC1:

<img width="759" alt="Screenshot 2022-12-09 at 21 46 00" src="https://user-images.githubusercontent.com/89082482/206771690-5c60a3fb-3e56-40f6-b494-7bd61cbd6cba.png">

На VPC2:

<img width="759" alt="Screenshot 2022-12-09 at 21 46 38" src="https://user-images.githubusercontent.com/89082482/206771777-f50d297e-ca78-4d35-8425-566ccd2f7bdf.png">

___________
Выводы show spanning-tree:

Switch3:

<img width="794" alt="Screenshot 2022-12-09 at 22 09 34" src="https://user-images.githubusercontent.com/89082482/206779184-113abe3a-58cc-4e7b-88b5-d7dfd215808a.png">

Switch4 блокирует порт между собой и Switch3:

<img width="794" alt="Screenshot 2022-12-09 at 22 07 19" src="https://user-images.githubusercontent.com/89082482/206778510-7160e20b-56a1-41c5-bf17-ed9746b47416.png">


Switch5 имеет наименьший приоритет и является корневым для VLAN 10 и 20:

<img width="794" alt="Screenshot 2022-12-09 at 22 03 57" src="https://user-images.githubusercontent.com/89082482/206777421-a3430d5c-039f-44eb-ae99-22c283833355.png">
