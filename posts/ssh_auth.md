Создаение автоматической авторизации. Сюда копируем публичный ключ пользователя

```

mkdir ~/.ssh

chmod 0700 ~/.ssh

touch ~/.ssh/authorized_keys

chmod 0644 ~/.ssh/authorized_keys



```

Или

```

mkdir ~/.ssh && chmod 0700 ~/.ssh && touch ~/.ssh/authorized_keys && chmod 0644 ~/.ssh/authorized_keys

```

Генерируем новую пару кличей  

```

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

```



Проходим аутентификацию по SSH, используем приватный ключь пользователя :

```

ssh -i privat.key -p 2211 root@34.226.134.81

```

Делаем id_rsa 

```

chmod 400 ~/.ssh/id_rsa

```
