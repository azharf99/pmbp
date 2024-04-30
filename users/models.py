from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.urls import reverse
from utilities.utils import CompressedImageField
from choices import jenis_kelamin, pilih_kelas
from time import time

def get_upload_file_name(instance, filename, folder=""):
    return "%s/%s_%s" % (folder, str(time()).replace('.','_'), filename)

class Teachers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Username"))
    teacher_id = models.IntegerField(default=0, verbose_name=_('Teacher Unique Number (NIY)'))
    teacher_code = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Teacher Code"))
    teacher_name = models.CharField(max_length=100, verbose_name=_("Teacher Name"))
    teacher_gender = models.CharField(max_length=1, choices=jenis_kelamin, verbose_name=_("Teacher Gender"))
    teacher_address = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Teacher Address"))
    teacher_job = models.CharField(max_length=100, blank=True, verbose_name=_("Teacher Job"))
    teacher_email = models.EmailField(default='smaitalbinaa.ekskul@outlook.com', blank=True, verbose_name=_("Teacher Email"))
    teacher_phone = models.CharField(max_length=50, blank=True, default=0, verbose_name=_("Teacher Phone"))
    teacher_photo = CompressedImageField(upload_to=get_upload_file_name(folder='teacher'), default='blank-profile.png', blank=True, null=True, help_text="format foto .jpg/.jpeg", verbose_name=_("Teacher Photo"))
    is_active = models.BooleanField(default=True, verbose_name=_("Teacher Active Status"))
    is_online = models.BooleanField(default=False, verbose_name=_("Teacher Online Status"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacher_name
    

    def get_absolute_url(self):
        return reverse("users:teacher-detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")
        ordering = ["teacher_name"]
        db_table = "teachers"



class Students(models.Model):
    student_nis = models.CharField(max_length=20, unique=True, verbose_name=_("Student's Unique Number (NIS)"))
    student_nisn = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("National Student's Unique Number (NISN)"))
    student_nik = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("Student's Family Unique Number (NIK)"))
    student_name = models.CharField(max_length=100, verbose_name=_("Student Name"))
    student_class = models.CharField(max_length=100, choices=pilih_kelas, blank=True, null=True, verbose_name=_("Student's Class"))
    student_gender = models.CharField(max_length=10, choices=jenis_kelamin, verbose_name=_("Student's Gender"))
    student_address = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("Student's Address"))
    student_birth_place = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Student's Birth Place"))
    student_birth_date = models.DateField(blank=True, null=True, verbose_name=_("Student's Birth Date"))
    student_email = models.EmailField(max_length=50, blank=True, null=True, verbose_name=_("Student's Email"))
    student_phone = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Student's Phone"))
    student_status = models.CharField(max_length=50, blank=True, default="Aktif", verbose_name=_("Student's Status"))
    student_photo = CompressedImageField(upload_to=get_upload_file_name(folder='student'), blank=True, null=True, default='blank-profile.png', help_text="Format foto .jpg/.jpeg", verbose_name=_("Student's Photo"))
    student_batch = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_("Student's Batch"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_name} {self.student_nis} {self.academic_year}"


    def get_absolute_url(self):
        return reverse("users:student-detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["student_nis", "id",]),
        ]
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
        ordering = ["student_class__full_name", "student_name"]
        db_table = "students"





