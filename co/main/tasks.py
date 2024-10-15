from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email(name, email, message):
    subject = f"Contact Form Submission from {name}"
    body = f"Name: {name}\nPhone: {email}\nMessage:\n{message}"
    send_mail(subject, body, 'komy.kabachok@yandex.ru', [EMAIL_HOST_USER])