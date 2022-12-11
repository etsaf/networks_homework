Комментарии и описание ниже в Readme, конфиги всех устройств в папке configs, сама выгруженная лаба - файл homework42.unl

**Топология**

<img width="837" alt="image" src="https://user-images.githubusercontent.com/89082482/206925014-6baebf9c-451a-47f0-9af9-24a5fba1a4ba.png">

**Настройки на устройствах**

VPC1:

```
ip 10.0.0.2 255.255.255.0 10.0.0.1
save
```

VPC2:

```
ip 20.0.0.2 255.255.255.0 20.0.0.1
save
```

VPC3:

```
ip 30.0.0.2 255.255.255.0 30.0.0.1
save
```


Internet:

```
enable
configure terminal

interface e0/0
no shutdown
ip address 100.0.0.254 255.255.255.0

interface e0/1
no shutdown
ip address 200.0.0.254 255.255.255.0

interface e0/2
no shutdown
ip address 150.0.0.254 255.255.255.0

exit
exit
wr
```

Router1:

```
enable
configure terminal

#configure interfaces
interface e0/0
no shutdown
ip address 10.0.0.1 255.255.255.0

interface e0/1
no shutdown
ip address 100.0.0.1 255.255.255.0
exit

#configure GRE to Router2
interface tunnel 200
tunnel mode gre ip
ip address 172.17.3.1 255.255.255.0
tunnel source 100.0.0.1
tunnel destination 200.0.0.1
ip mtu 1400
ip tcp adjust-mss 1360
exit

#configure route and default
ip route 20.0.0.0 255.255.255.0 172.17.3.2
ip route 0.0.0.0 0.0.0.0 100.0.0.254


#configure GRE to Router3
interface tunnel 300
no shutdown
tunnel mode gre ip
ip address 173.17.3.1 255.255.255.0
tunnel source 100.0.0.1
tunnel destination 150.0.0.1
ip mtu 1400
ip tcp adjust-mss 1360
exit

#configure route
ip route 30.0.0.0 255.255.255.0 173.17.3.2

#configure ISAKMP

crypto isakmp policy 10
authentication pre-share
encryption aes
group 2
hash sha256
exit

crypto isakmp key secret address 150.0.0.1

#configure IPSec
crypto ipsec transform-set TFS esp-aes esp-sha256-hmac
exit
crypto ipsec profile PF
set transform-set TFS
exit

#apply to GRE
interface tunnel 300
tunnel protection ipsec profile PF
exit

wr

```

Router2:

```
enable
configure terminal

#configure interfaces
interface e0/0
no shutdown
ip address 200.0.0.1 255.255.255.0

interface e0/1
no shutdown
ip address 20.0.0.1 255.255.255.0
exit

#configure GRE
interface tunnel 200
no shutdown
tunnel mode gre ip
ip address 172.17.3.2 255.255.255.0
tunnel source 200.0.0.1
tunnel destination 100.0.0.1
ip mtu 1400
ip tcp adjust-mss 1360
exit

#configure route and default
ip route 10.0.0.0 255.255.255.0 tunnel 200
ip route 0.0.0.0 0.0.0.0 200.0.0.254
exit
wr
```

Router3:

```
enable
configure terminal

#configure interfaces
interface e0/0
no shutdown
ip address 150.0.0.1 255.255.255.0

interface e0/1
no shutdown
ip address 30.0.0.1 255.255.255.0
exit

#configure GRE
interface tunnel 300
no shutdown
tunnel mode gre ip
ip address 173.17.3.2 255.255.255.0
tunnel source 150.0.0.1
tunnel destination 100.0.0.1
ip mtu 1400
ip tcp adjust-mss 1360
exit

#configure route and default
ip route 10.0.0.0 255.255.255.0 173.17.3.1
ip route 0.0.0.0 0.0.0.0 150.0.0.254
exit

#configure ISAKMP

crypto isakmp policy 10
authentication pre-share
encryption aes
group 2
hash sha256
exit

crypto isakmp key secret address 100.0.0.1

#configure IPSec
crypto ipsec transform-set TFS esp-aes esp-sha256-hmac
exit
crypto ipsec profile PF
set transform-set TFS
exit

#apply to GRE
interface tunnel 300
tunnel protection ipsec profile PF
exit
wr

```

**Вывобы с устройств**

С VPC1 проходит ping на VPC2 и VPC3 и обратно

<img width="946" alt="Screenshot 2022-12-11 at 21 57 08" src="https://user-images.githubusercontent.com/89082482/206923206-02184ce8-e87e-4813-8fb2-de053e3262ba.png">

На Router1 работает GRE-тоннель к Router2

<img width="919" alt="Screenshot 2022-12-11 at 23 02 32" src="https://user-images.githubusercontent.com/89082482/206926072-67346c2b-bb22-4c99-a266-5c1f241d46e6.png">

Он же на Router2

<img width="919" alt="Screenshot 2022-12-11 at 23 04 38" src="https://user-images.githubusercontent.com/89082482/206926163-c67352fd-434e-4ab2-a4aa-94b9ae5b6e0a.png">

На Router1 подключен GRE-тоннель поверх IPSec к Router3:

<img width="946" alt="Screenshot 2022-12-11 at 21 58 39" src="https://user-images.githubusercontent.com/89082482/206923269-7b88627d-9166-48b1-9fb0-e8250f39e718.png">

<img width="946" alt="Screenshot 2022-12-11 at 21 49 24" src="https://user-images.githubusercontent.com/89082482/206922832-d5ad5473-04a0-4104-b7cf-4a7b2060f0ee.png">

Он же на Router3

<img width="946" alt="Screenshot 2022-12-11 at 21 50 03" src="https://user-images.githubusercontent.com/89082482/206922869-82ea359b-b09a-4e58-ba87-d89055a3d796.png">

<img width="946" alt="Screenshot 2022-12-11 at 21 50 30" src="https://user-images.githubusercontent.com/89082482/206922883-f161142d-4dd1-4111-895d-951529c990ec.png">
