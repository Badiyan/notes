﻿sudo (англ. substitute user and do, дословно «подменить пользователя и выполнить») — программа для системного администрирования UNIX-систем, позволяющая делегировать те или иные привилегированные ресурсы пользователям с ведением протокола работы. Основная идея — дать пользователям как можно меньше прав, при этом достаточных для решения поставленных задач. Программа поставляется для большинства UNIX и UNIX-подобных операционных систем.





Добавляем возможность автоматического входа в права root: 

```

 vim /etc/sudoers

login_name   ALL=(ALL) NOPASSWD:ALL

```

А еще можно так: 

```

usermod -a -G sudo username

```

###Сделать так чтобы  человек сменил  пароль при первом входе в систему.

```

# passwd --expire user 

```

Дальше смотрим 

```

# chage -l ravi

```

также другой способ, меняем срок действия пароля :

```

# chage --lastday 0 user 

```

или 

```

# chage --lastday 1970-01-01 user

```

смотрим

```

# chage -l user

```

Полезная статья 

https://habr.com/post/122445/