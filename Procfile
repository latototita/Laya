web: gunicorn Eshop.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
python manage.py makemigrations
manage.py migrate

python manage.py createsuperuser
