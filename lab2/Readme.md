**Как использовать**

Чтобы создать docker image:

```
docker build -t find_mtu .
```

Чтобы запустить созданный образ (вместо _hostname_ нужно вписать имя искомого хоста):

```
docker run find_mtu hostname
```

Пример работы на MacOS:

<img width="582" alt="Screenshot 2022-12-10 at 15 25 14" src="https://user-images.githubusercontent.com/89082482/206854976-f8a01a00-b6e2-4204-aa4c-1c3a748dd89f.png">
