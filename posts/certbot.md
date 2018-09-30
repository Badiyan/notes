Certbot 
----

```

certbot revoke --cert-path /etc/letsencrypt/live/test.amurchik.ua/cert.pem

Удаляет все ведомости о выданном сертификате из базы центра letsencrypt



certbot delete --cert-name test.amurchik.ua

Удаляет конфиги, сертификаты и линки из сервера



Добавил в iptables разрешающее правило для порта 80

certbot certonly --webroot -w /var/www/html/ -d test.amurchik.ua --dry-run - как только видим что всё ок - убираем --dry-run

Убрал правило из iptables

```