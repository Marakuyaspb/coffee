from django.contrib import admin
from .models import *

@admin.register(CallMe)
class CallMeAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'phone', 'message', 'created']