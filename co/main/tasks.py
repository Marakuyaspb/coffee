from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_email(name, phone, message):
    subject = f"С сайта coffeeinveins пишет {name}"
    body = f"Имя: {name}\n\nТелефон: {phone}\n\nСообщение:\n{message}"
    recipient_list = ['to.the.neizvestnost@yandex.ru']

    try:
        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)
        logger.info(f"Email sent from {name}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")