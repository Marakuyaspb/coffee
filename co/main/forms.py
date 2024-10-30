from django import forms
from .models import *


class CallMeForm(forms.ModelForm):
    class Meta:
        model = CallMe
        fields = ['first_name', 'phone', 'message']
        labels = {
        'first_name': 'Имя',
        'phone': 'Телефон',
        'message': 'Комментарий',
        }