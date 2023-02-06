## start

```shell
cp .env.example .env
# update SECRET_KEY DATABASE_URL

python manage.py makemigrations
python manage.py migrate --run-sync
python manage.py createsuperuser
python manage.py collectstatic

nohup gunicorn -b 127.0.0.1:8005 dj_server.wsgi >>log 2>&1 &
```

```shell
# supervisor config

[program:django]

directory = /home/user/django_demo
command = /home/user/.venv/py3/bin/gunicorn -b 127.0.0.1:8005 dj_server.wsgi
user = user
autostart = true
autorestart = unexpected
startsecs   = 3
```

[![simpleui](https://img.shields.io/badge/developing%20with-Simpleui-2077ff.svg)](https://github.com/newpanjing/simpleui)
