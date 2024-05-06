from django.contrib import admin
from .models import OlympiadField, OlympiadReport, OlympiadStudent
# Register your models here.

admin.site.register(OlympiadField)
admin.site.register(OlympiadReport)
admin.site.register(OlympiadStudent)
