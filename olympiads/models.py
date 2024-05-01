from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from extracurricular.models import Teacher, Student
from utilities.utils import CompressedImageField
from utilities.filenames import get_upload_file_name


# Create your models here.

class OlympiadField(models.Model):
    olympiad_field_name = models.CharField(max_length=50, verbose_name=_("Olympiad Field's Name"))
    olympiad_field_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name=_("Olympiad Field's Teacher"))
    olympiad_field_schedule = models.TextField(max_length=200, verbose_name=_("Olympiad Field's Schedule"))
    slug = models.SlugField(_("Olympiad Field's Schedule"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.olympiad_field_name}"
    
    def get_absolute_url(self):
        return reverse("olympiads:olympiad-detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Olympiad Field")
        verbose_name_plural = _("Olympiad Fields")
        ordering = ["olympiad_field_name"]
        db_table = "olympiad_fields"


class OlympiadStudent(models.Model):
    olympiad_field = models.ForeignKey(OlympiadField, on_delete=models.CASCADE, verbose_name=_("Olympiad Field"))
    olympiad_student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_("Student"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.olympiad_field} {self.olympiad_student}"
    
    def get_absolute_url(self):
        return reverse("olympiads:olympiad-student-detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Olympiad Student")
        verbose_name_plural = _("Olympiad Students")
        ordering = ["olympiad_field"]
        db_table = "olympiad_students"


class OlympiadReport(models.Model):
    olympiad_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=_("Olympiad Teacher"))
    olympiad_field = models.ForeignKey(OlympiadField, on_delete=models.CASCADE, verbose_name=_("Olympiad Field"))
    olympiad_practice_date = models.DateField(_("Olympiad Practice Date"))
    students = models.ManyToManyField(OlympiadStudent, verbose_name=_("Student's Presence"))
    photo = CompressedImageField(upload_to=get_upload_file_name('ekskul/osn'), default='no-image.png', quality=50, help_text=_("photo format png/jpg"), verbose_name=_("Upload Photo"))
    notes = models.TextField(max_length=200, blank=True, verbose_name=_("Notes"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.olympiad_practice_date.__format__("%d %B %Y")} {self.olympiad_teacher}'
    
    def get_absolute_url(self):
        return reverse("olympiads:olympiad-report-detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Olympiad Report")
        verbose_name_plural = _("Olympiad Reports")
        ordering = ["-olympiad_practice_date"]
        db_table = "olympiad_reports"
