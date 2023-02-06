#!/bin/sh

if [ -z "$1" ]; then
  echo "no args"
  nohup gunicorn -b 127.0.0.1:8005 dj_server.wsgi >>log 2>&1 &
else
  echo $1
  nohup  gunicorn -b 127.0.0.1:$1 dj_server.wsgi >> log 2>&1 &
  # gunicorn -b 127.0.0.1:$1 dj_server.wsgi
fi
