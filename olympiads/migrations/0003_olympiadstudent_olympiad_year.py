# Generated by Django 5.0.4 on 2024-05-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympiads', '0002_remove_olympiadreport_olympiad_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='olympiadstudent',
            name='olympiad_year',
            field=models.CharField(default=2024, max_length=15, verbose_name='Olympiad Year'),
        ),
    ]