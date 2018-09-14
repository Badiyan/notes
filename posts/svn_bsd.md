```

pkg install subversion

#Для использования метода https

pkg install ca_root_nss

rm -rf /usr/src

svn co https://svn.freebsd.org/base/head /usr/src

rm -rf /usr/doc

svn co https://svn.freebsd.org/doc/head /usr/doc

rm -rf /usr/ports

svn co https://svn.freebsd.org/ports/head /usr/ports



```