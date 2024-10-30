FROM python:3.10-slim-bullseye

WORKDIR /co
COPY ./co/requirements.txt /co/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./co  /co
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]