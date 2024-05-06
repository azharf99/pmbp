from django.contrib import admin
from .models import Extracurricular, StudentExtracurricular, TeacherExtracurricular

# Register your models here.

admin.site.register(Extracurricular)
admin.site.register(StudentExtracurricular)
admin.site.register(TeacherExtracurricular)
