import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .form_generator import *


def index(request):
	callme_form = handle_callme_form(request)
	context = {
		'callme_form': callme_form,
	}
	return render(request, 'main/index.html', context)


def privacy(request):
	return render(request, 'main/privacy.html')