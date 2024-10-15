import os
import logging
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.template import loader

from .forms import *
from .models import *
from .tasks import * 

logging.basicConfig(filename='mail_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')


def handle_callme_form(request):
    if request.method == 'POST':
        callme_form = CallMeForm(request.POST)
        if callme_form.is_valid():
            callme_order = callme_form.save()

            context = {
                'callme_order': callme_order,
            }

            try:
                send_mail(
                    'New message',
                    'Ni!!',
                    settings.EMAIL_HOST_USER,
                    ['komy.kabachok@yandex.ru'],
                    fail_silently=True,
                    html_message=loader.get_template('main/mail.html').render(context)
                )
                logging.info("Mail to manager sent successfully!!!")
            except Exception as e:
                logging.error(f"Error sending mail to: {str(e)}")

            return callme_form
    else:
        callme_form = CallMeForm()

    return callme_form