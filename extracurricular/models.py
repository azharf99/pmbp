from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _
from django.utils.dates import WEEKDAYS
from django.utils.text import slugify
from users.models import Student, Teacher
from utilities.choices import extracurricular_types, extracurricular_times
from utilities.utils import CompressedImageField
from utilities.filenames import get_upload_file_name

# Create your models here.
class Extracurricular(models.Model):
    extracurricular_name = models.CharField(max_length=50, verbose_name=_("Extracurricular Name"))
    extracurricular_schedule = models.CharField(max_length=15, choices=WEEKDAYS, verbose_name=_("Extracurricular Schedule"))
    extracurricular_time = models.CharField(max_length=15, choices=extracurricular_times, verbose_name=_("Extracurricular Iime"))
    extracurricular_description = models.TextField(blank=True, null=True, verbose_name=_("Extracurricular Description"))
    extracurricular_type = models.CharField(max_length=20, choices=extracurricular_types, blank=True, verbose_name=_("Extracurricular Type"))
    extracurricular_logo = CompressedImageField(upload_to=get_upload_file_name('ekskul/logo'), default='no-image.png', blank=True, null=True, quality=50, help_text=_("photo format png/jpg"), verbose_name=_("Extracurricular Logo"))
    slug = models.SlugField(blank=True, verbose_name=_("Extracurricular Slug"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.extracurricular_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.extracurricular_name)
        super(Extracurricular, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("extracurricular:extracurricular-detail", kwargs={"slug": self.slug})

    class Meta:
        indexes = [
            models.Index(fields=["id", "slug",]),
        ]
        verbose_name = _("Extracurricular")
        verbose_name_plural = _("Extracurricular Activities")
        ordering = ["extracurricular_name"]
        db_table = "extracurricular"


class StudentExtracurricular(models.Model):
    extracurricular = models.ForeignKey(Extracurricular, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.extracurricular} {self.student}"

    def get_absolute_url(self):
        return reverse("extracurricular:student-extracurricular-index")
    
    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Student Extracurricular")
        verbose_name_plural = _("Student Extracurricular Activities")
        ordering = ["extracurricular__extracurricular_name"]
        db_table = "extracurricular_students"


class TeacherExtracurricular(models.Model):
    extracurricular = models.ForeignKey(Extracurricular, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.extracurricular} {self.teacher}"

    def get_absolute_url(self):
        return reverse("extracurricular:teacher-extracurricular-index")
    
    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Teacher Extracurricular")
        verbose_name_plural = _("Teacher Extracurricular Activities")
        ordering = ["extracurricular__extracurricular_name"]
        db_table = "extracurricular_teachers"