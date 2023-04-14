#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json

# from generate_apis.main import main as generate_apis


def main():
    print("argv:", sys.argv)
    commands = {
        "mm": "python manage.py makemigrations",
        "mr": "python manage.py migrate",
        "mrs": "python manage.py migrate --run-syncdb",
        "st": "python manage.py collectstatic -c",
        "all": "python manage.py makemigrations && python manage.py migrate --run-syncdb && rm -rf staticfiles && python manage.py collectstatic -c",
        "gen": "python manage.py init_admin && python manage.py gen_all && cd tyadmin && yarn install && yarn build",
        "cs": "python manage.py createsuperuser --email ycm76229@gmail.com --username ycm76229",
        "dev": "open http://127.0.0.1:8000/ && python manage.py runserver 0.0.0.0:8000",
        "start": "gunicorn -w 8 -b localhost:8000 dj_server.wsgi",
    }
    # functions = {"generate": generate_apis}
    functions = {}

    if len(sys.argv) < 2:
        print("commands: ", json.dumps(commands, indent=2, ensure_ascii=False))
        print("functions: ", json.dumps({k: v.__module__ for k, v in functions.items()}, indent=2, ensure_ascii=False))
    elif sys.argv[1] in commands.keys():
        os.system(commands[sys.argv[1]])
    elif sys.argv[1] in functions.keys():
        functions[sys.argv[1]]()
    else:
        """Run administrative tasks."""
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_server.settings")
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
