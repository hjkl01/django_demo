python manage.py makemigrations && python manage.py migrate
python manage.py createsuperuser

python manage.py collectstatic

gunicorn -w 8 -b localhost:8000 data_service.wsgi
or
./start.sh {port}

questions:
    python manage.py migrate --run-syncdb
