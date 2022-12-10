**Как использовать**

Чтобы создать docker image:

```
docker build -t find_mtu .
```

Чтобы запустить созданный образ (вместо _hostname_ нужно вписать имя искомого хоста):

```
docker run find_mtu hostname
```

Пример работы и сравнение с результатом ping на macOS. Почему такой низкий MTU для google, не знаю :(

<img width="584" alt="image" src="https://user-images.githubusercontent.com/89082482/206854227-8aa7287d-e1f2-431d-a8c5-9cf9f297e4b6.png">
<img width="582" alt="Screenshot 2022-12-10 at 15 13 46" src="https://user-images.githubusercontent.com/89082482/206854556-2ee91621-4bc1-4077-8e9d-2ea97eb1bfd2.png">
