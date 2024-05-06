from django.db import models
from django.urls import reverse
from django.utils import timezone
from extracurricular.models import StudentExtracurricular
from django.utils.translation import gettext as _
from utilities.choices import semester_choice, grade_choice


# Create your models here.
class Grade(models.Model):
    student = models.ForeignKey(StudentExtracurricular, on_delete=models.CASCADE, verbose_name=_("Student Name"))
    grade = models.CharField(max_length=3, choices=grade_choice, verbose_name=_("Grade"))
    semester = models.CharField(max_length=10, choices=semester_choice, blank=True, null=True, verbose_name=_("Semester"))
    academic_year = models.CharField(max_length=50, default=f"{timezone.now().year}/{timezone.now().year+1}", verbose_name=_("Academic Year"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} {self.grade}"

    def get_absolute_url(self):
        return reverse("grades:grade-detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Grade")
        verbose_name_plural = _("Grades")
        ordering = ["student"]
        db_table = "grades"