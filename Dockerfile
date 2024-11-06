FROM python:3.10-slim-bullseye

WORKDIR /co

COPY ./co/requirements.txt /co/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./co /co

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn co.wsgi:application --bind 0.0.0.0:8000 --log-level info"]