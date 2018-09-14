делимся секретом  

```

vault read -wrap-ttl-10m secret/my_secret 

```



```

  $ export VAULT_ADDR='http://127.0.0.1:8200'



root@debian9-tpl:~# export VAULT_ADDR='http://0.0.0.0:8200'

root@debian9-tpl:~# vault operator init

Unseal Key 1: 1ZzaGFwlTlExIAtz00crqCSZl1s6SFP/wRe7YB+WM32/

Unseal Key 2: VQGTz94wp7Paq/GDTl1ypeUGBW2+9/QGbgF48nDryFSP

Unseal Key 3: i5+pNwYWZDT2G1RPrwXhB4T2sQ7EsTysiW1dQUy0IjUc

Unseal Key 4: 0m8nF8Q32Y1ICP5aS8hZ3r45MbST/HSgmGQWpZYbavUN

Unseal Key 5: 2n9wrQ7SEZ3NkEPMOBILtVHBjuw/c7d8vY5ZFvjWzKIU



Initial Root Token: b6d2a47e-f3b1-0ee9-e61f-5a10836b1f71





root@debian9-tpl:~# vault write -f -wrap-ttl=20m -format=json auth/approle/role/goldfish/secret-id



nohup ./goldfish -config=config.hcl

vault server -config=vault.config.hcl



root_token 5dc43058-f2ad-a438-2c98-72e7ae4be8dd

eleutherius root token 5dc43058-f2ad-a438-2c11-72e7ae4baabb

```

#####windows

```

 set VAULT_ADDR=http://vault-nf.ml:8200

 vault login 5dc43058-f2ad-a438-2c11-72e7ae4baabb

```





## Презентация 

#### План

- Что есть  и почему так быть не должно  

- Какие есть  ппрограммы и почему они не подходят.   

#### Hasicorp Vault  

 - Что из себя представляет   

- Основные плюшки 

    - Централизированое место  управления секретами 

    - Гибкие ACL для команды/инвайромента 

    - Интеграция с тулзами которые  мы используем (Kubernetes,  AWS, Jankins, Ansible, Docker, CHEF, Pappet )

    - Можно шифровать свои данные и хранить на Dropbox.

    - Адекватный UI/Cli интерфейс  

    - Безопасность, шифрование данных.  

    -  Динамический доступ к паролям. (продвинутое использование)



#### Как использовать 

Смотрим свой статус 

```

vault status

```

Смотрим доступные папки паролей

```

vault secrets list

``` 

Читаем определенное значение   



```

 vault read secret/adoriasoft/wise-wolf/wise-wolf_dev/mysql

```

Запишем  что-то по выбранному пути 

```

vault write  secret/adoriasoft/wise-wolf/ name1=1234 name2=1234

vault read  secret/adoriasoft/wise-wolf

```

Смотрим help по каждому пути 

```

vault secrets enable -path=aws aws

vault path-help aws

```
