from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_email(name, phone, message):
    subject = f"Contact Form Submission from {name}"
    body = f"Name: {name}\nPhone: {phone}\nMessage:\n{message}"

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, ['to.the.neizvestnost@yandex.ru'])
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")