from django.db import models
from django.urls import reverse
from utilities.utils import CompressedImageField
from users.models import Student
from django.utils.translation import gettext as _

# Create your models here.
class Achievement(models.Model):
    champion_name = models.CharField(max_length=100, verbose_name=_("The Champion's Name"))
    competition_name = models.CharField(max_length=100, verbose_name=_("Competition Name"))
    champion_class = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("The Champion's Class"), help_text=_("optional"))
    champion_level = models.CharField(max_length=100, verbose_name=_("Champion Level Category"))
    competition_level = models.CharField(max_length=100, verbose_name=_("Field of Competition"))
    achievement_category = models.CharField(max_length=100, verbose_name=_("Achievement Category"))
    competition_type = models.CharField(max_length=100, verbose_name=_("Competition Type"))
    competition_level = models.CharField(max_length=100, verbose_name=_("Competition Level"))
    competition_date = models.CharField(max_length=10, verbose_name=_("Competition Date"))
    competition_organizer = models.CharField(max_length=100, verbose_name=_("Achievement Organizer"))
    school = models.CharField(max_length=100, default="SMAS IT Al Binaa", verbose_name=_("School"))
    certificate = models.FileField(upload_to='prestasi/sertifikat', null=True, blank=True, verbose_name=_("Achievement Certificate"), help_text=_("file format pdf/jpg"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.champion_level} {self.competition_name} {self.competition_date} {self.champion_name}"
    
    def get_absolute_url(self):
        return reverse("achievements:achievement-detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Achievement")
        verbose_name_plural = _("Achievements")
        ordering = ["-competition_date"]
        db_table = "achievements"


class AchievementPhoto(models.Model):
    achievement = models.ForeignKey('Prestasi', on_delete=models.CASCADE, verbose_name=_("Achievement"))
    achievement_photo = CompressedImageField(upload_to='prestasi', blank=True, null=True, default='no-image.png', verbose_name=_("Achievement Photo"))
    achievement_notes = models.TextField(max_length=300, blank=True, null=True, default="", verbose_name=_("Achievement Notes"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.achievement}"

    def get_absolute_url(self):
        return reverse("achievements:achievement-photo-detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Achievement Photo")
        verbose_name_plural = _("Achievement Photos")
        ordering = ["-created_at"]
        db_table = "achievement_photos"


class AchievementProgram(models.Model):
    achievement_program = models.CharField(max_length=200, verbose_name=_("Achievement Program"))
    program_date = models.DateField(_("Program Date"))
    students = models.ManyToManyField(Student, verbose_name=_("Students"))
    achievement = models.CharField(max_length=200, verbose_name=_("Achievement"))
    notes = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Notes"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.achievement_program
    

    def get_absolute_url(self):
        return reverse("achievements:achievement-program-detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Achievement Program")
        verbose_name_plural = _("Achievement Programs")
        ordering = ["-created_at"]
        db_table = "achievement_programs"