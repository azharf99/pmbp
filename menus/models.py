from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.
class Menu(models.Model):
    url_name = models.CharField(max_length=100, verbose_name=_("Url Name"))
    menu_title = models.CharField(max_length=100, verbose_name=_("Menu Title"))
    menu_arabic_title = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Arabic Title"))
    icon_data = models.TextField(max_length=1500, blank=True, null=True, verbose_name=_("Icon data"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.menu_title} | {self.url_name}"

    def get_absolute_url(self):
        return reverse('menus:menu-index')

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
        ]
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")
        ordering = ["menu_title"]
        db_table = "menus"
