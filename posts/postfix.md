1) Создать  DNS записи. 

A - запись например  "teneta.ml"

MX - запись

PTR - запись 

```

 nslookup -type=PTR 195.69.86.94

```

Есть postfix - он smtp - предназначен для отправки почты, у него есть своя база пользователей, в которой написано с каким логином и паролем они должны подключаться.

Есть dovecot - он pop3 - предназначен для приёма почты. У него есть такая же база, где написаны креды (логин и пароль) для пользователей.

Есть roudcube - он IMAP - предназначен для управления (отправка через smtp и получение через pop3) почты с web. У него тоже есть своя база с логинами и паролями.

Ко всему этому есть ssl, который подключается для шифрования канала, в следствии чего меняется порт. Например, для smtp это 443, 587. Для POP3 - это 993, 995, 143

Есть ещё панель управления, она называется postfixadmin, подходит почти для всех smtp, с панели можно создавать новых пользователей и управлять ими.



Для использования Postfixadmin, Postfix должен иметь mysql или postgres модуль - ``` postconf -m```





###Проверка авторизации и получения почты (Dovecot)

```

$ telnet 77.120.106.40 110>

Trying 77.120.106.40...

Connected to 77.120.106.40.

Escape character is '^]'.

+OK Dovecot ready.

user admin@website.co.ua // вводим логин

+OK

pass mypassword // вводим пароль

+OK Logged in.

list // вывести список писем и папок

+OK 3 messages:

1 672// письмо номер 1, с размером 672 байта

2 276

3 283

.

retr 1 // открыть письмо 1 для прочтения

+OK 672 octets

Return-Path: <admin@website.co.ua>

Delivered-To: admin@website.co.ua

Received: from website.co.ua (localhost [127.0.0.1])

by mail.website.co.ua (Postfix) with ESMTP id 47C403F41B

for <admin@website.co.ua>; Tue, 17 Jan 2012 18:29:11 +0200 (EET)

To: admin@website.co.ua

From: admin@website.co.ua

Subject: =?UTF-8?Q?=D0=94=D0=BE=D0=B1=D1=80=D0=BE=20=D0=BF=D0=BE=D0=B6=D0=B0=D0=BB?=

=?UTF-8?Q?=D0=BE=D0=B2=D0=B0=D1=82=D1=8C!?=

MIME-Version: 1.0

Content-Type: text/plain; charset=utf-8

Content-Transfer-Encoding: 8bit

Message-Id: <20120117162911.47C403F41B@mail.website.co.ua>

Date: Tue, 17 Jan 2012 18:29:11 +0200 (EET)



Hi,

Welcome to your new account.

.

retr 2 //открыть письмо 2 для прочтения

+OK 276 octets

Return-Path: <admin@website.co.ua>

Delivered-To: admin@website.co.ua

Received: from 82.144.220.27 (nat.merlin.dc.volia.com [82.144.220.27])

by mail.website.co.ua (Postfix) with SMTP id 768273F408

for <admin@website.co.ua>; Tue, 17 Jan 2012 18:43:20 +0200 (EET)

test

.

quit //выходим

+OK Logging out.

Connection closed by foreign host.

```

Для подключения к SMTP серверу с защитой TLS используйте:





$ openssl s_client -connect remote.host:25 -starttls smtp

Проверка отправки почты (Postfix/Exim)

```

$ telnet 77.120.106.40 25

Trying 77.120.106.40...

Connected to 77.120.106.40.

Escape character is '^]'.

220 mail.website.co.ua ESMTP Postfix

helo 195.69.86.86 //поприветствуем друг-друга

250 mail.website.co.ua

mail from:telli@teneta.ml //начнем писать письмо, указываем отправителя (наш адрес)

250 2.1.0 Ok 



rcpt to:telli@teneta.ml  //указываем получателя

250 2.1.5 Ok

data //указываем, что дальше пойдет текст письма

354 End data with <CR><LF>.<CR><LF>

test letter //сам текст

.//что бы закончить текст, в новой строке ставим точку и нажимаем Enter

250 2.0.0 Ok: queued as C78363F408 //письмо принято к отправке под номером  C78363F408

quit

221 2.0.0 Bye

Connection closed by foreign host.

```

Посмотрим логи почтового сервера:



```

view source

# less /var/log/maillog

Jan 17 19:20:22 akira postfix/smtpd[1521]: C78363F408: client=nat.merlin.dc.volia.com[82.144.220.27]

Jan 17 19:20:31 akira postfix/cleanup[1530]: C78363F408: message-id=<>

Jan 17 19:20:31 akira postfix/qmgr[1213]: C78363F408: from=<admin@website.co.ua>, size=212, nrcpt=1 (queue active)

Jan 17 19:20:31 akira dovecot: auth-worker: mysql(127.0.0.1): Connected to database postfix

Jan 17 19:20:31 akira dovecot: lda(admin@website.co.ua): msgid=unspecified: saved mail to INBOX

Jan 17 19:20:31 akira postfix/pipe[1531]: C78363F408: to=<admin@website.co.ua>, relay=dovecot, delay=31, delays=31/0.01/0/0.03, dsn=2.0.0, status=sent (delivered via dovecot service)

Jan 17 19:20:31 akira postfix/qmgr[1213]: C78363F408: removed

Jan 17 19:20:44 akira postfix/smtpd[1521]: disconnect from nat.merlin.dc.volia.com[82.144.220.27]

```



Отправляем письмо через консоль: 

```

 echo "test email" | mail -s "Сранное письмо!" eleutherius69@gmail.com

```