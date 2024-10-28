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

            name = callme_order.first_name
            phone = callme_order.phone 
            message = callme_order.message

            # Call the Celery task
            send_email.delay(name, phone, message)
            
            return callme_form
    else:
        callme_form = CallMeForm()

    return callme_form