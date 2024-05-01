from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _
from users.models import Teacher
from extracurricular.models import Extracurricular, StudentExtracurricular
from utilities.utils import CompressedImageField
from utilities.filenames import get_upload_file_name

# Create your models here.

class Report(models.Model):
    extracurricular = models.ForeignKey(Extracurricular, on_delete=models.CASCADE, verbose_name=_("Extracurricular Name"))
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=_("Teacher"))
    report_date = models.DateField(verbose_name=_("Report Date"))
    report_note = models.TextField(max_length=200, blank=True, verbose_name=_("Report Note"))
    students = models.ManyToManyField(StudentExtracurricular, verbose_name=_("Students"))
    report_photo = CompressedImageField(upload_to=get_upload_file_name('ekskul/laporan'), default='no-image.png', quality=50, help_text=_("photo format png/jpg"), verbose_name=_("Report Photo"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.report_date.__format__("%d %B %Y")} {self.extracurricular}'

    def get_absolute_url(self):
        return reverse("reports:report-detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Report")
        verbose_name_plural = _("Reports")
        ordering = ["-report_date"]
        db_table = "reports"