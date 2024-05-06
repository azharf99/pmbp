from django.contrib import admin
from .models import Achievement, AchievementPhoto, AchievementProgram

# Register your models here.

admin.site.register(Achievement)
admin.site.register(AchievementPhoto)
admin.site.register(AchievementProgram)
