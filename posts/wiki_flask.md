Устанавилваем необходиміе комплектуюющие:

- python3 

- nginx 

- uwsgi + uwsgi plagins 





configs : 

```

cat /etc/nginx/sites-available/wiki.conf

upstream flask_serv {

    server unix:/run/uwsgi/app/wiki/wiki.sock;

}



server {

    access_log /var/log/nginx/wiki_access.log;

    error_log /var/log/nginx/wiki_error.log;

    listen 80;

    server_name _;



    location / {

        uwsgi_pass flask_serv;

        include uwsgi_params;

    }



#    location /static/ {

#        root /var/www/patric/wiki_flask/wiki/web/static/;

#    }

}

```



```

 alex@teneta:/var/www/Flask-Wiki $ cat /etc/nginx/sites-available/wiki.conf

upstream flask_serv {

    server unix:/run/uwsgi/app/wiki/wiki.sock;

}



server {

    access_log /var/log/nginx/wiki_access.log;

    error_log /var/log/nginx/wiki_error.log;

    listen 80;

    server_name _;



    location / {

        uwsgi_pass flask_serv;

        include uwsgi_params;

    }



#    location /static/ {

#        root /var/www/patric/wiki_flask/wiki/web/static/;

#    }

}





(venv) alex@teneta:/var/www/Flask-Wiki $ cat /etc/uwsgi/apps-available/

README    wiki.xml

(venv) alex@teneta:/var/www/Flask-Wiki $ cat /etc/uwsgi/apps-available/wiki.xml

<uwsgi>

    <socket> /run/uwsgi/app/wiki/wiki.sock</socket>

    <pythonpath>/var/www/Flask-Wiki/</pythonpath>

    <module>application:app</module>

    <plugins>python3</plugins>

    <virtualenv>/var/www/Flask-Wiki/venv/</virtualenv>

    <app mountpoint="/var/www/Flask-Wiki/">



        <script>wsgi_configuration_module</script>



    </app>

    <master/>

    <processes>4</processes>

    <harakiri>60</harakiri>

    <reload-mercy>8</reload-mercy>

    <cpu-affinity>1</cpu-affinity>

    <stats>/tmp/stats.socket</stats>

    <max-requests>2000</max-requests>

    <limit-as>512</limit-as>

    <reload-on-as>256</reload-on-as>

    <reload-on-rss>192</reload-on-rss>

    <no-orphans/>

    <vacuum/>



</uwsgi>







```



###Возможные проблемы и способы решения:

- 1   Возможно нужно переименовать wiki.py в application.py

- 2  ```   [pid: 5447|app: 0|req: 9/12] 192.168.10.3 () {44 vars in 933 bytes} [Wed Apr 25 11:51:58 2018] GET /tags/ => generated 263 bytes in 22 msecs (HTTP/1.1 302) 4 headers in 389 bytes (2 switches on core 0)

    /var/www/Flask-Wiki/wiki/web/routes.py:134: FlaskWTFDeprecationWarning: "flask_wtf.Form" has been renamed to "FlaskForm" and will be removed in 1.0.

      form = LoginForm( ``` , тут делать ничего не нужно но так, заметка на будущее ... 

- 3  Изменить пути в config.py, поменять права на правильные  



Если есть проблемы с virtualenv, делаем так:

```

rm -rf venv

virtualenv -p /usr/bin/python3 venv/

source env/bin/activate

pip install -r requirements.txt

```