# Generated by Django 5.0.4 on 2024-04-30 18:42

import django.db.models.deletion
import utilities.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extracurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extracurricular_name', models.CharField(max_length=50, verbose_name='Extracurricular Name')),
                ('extracurricular_schedule', models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=15, verbose_name='Extracurricular Schedule')),
                ('extracurricular_time', models.CharField(choices=[('Pagi', 'Morning'), ('Siang', 'Evening'), ('Sore', 'Afternoon'), ('Malam', 'Night')], max_length=15, verbose_name='Extracurricular Iime')),
                ('extracurricular_description', models.TextField(blank=True, null=True, verbose_name='Extracurricular Description')),
                ('extracurricular_type', models.CharField(blank=True, choices=[('Ekskul', 'Extracurricular'), ('SC', 'Study Club')], max_length=20, verbose_name='Extracurricular Type')),
                ('extracurricular_logo', utilities.utils.CompressedImageField(blank=True, default='no-image.png', help_text='photo format png/jpg', null=True, quality=50, upload_to='ekskul/logo', verbose_name='Extracurricular Logo')),
                ('slug', models.SlugField(blank=True, verbose_name='Extracurricular Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extracurricular_teacher', models.ManyToManyField(to='users.teacher', verbose_name='Extracurricular Teacher')),
            ],
            options={
                'verbose_name': 'Extracurricular',
                'verbose_name_plural': 'Extracurricular Activities',
                'db_table': 'extracurricular',
                'ordering': ['extracurricular_name'],
            },
        ),
        migrations.CreateModel(
            name='StudentExtracurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(default='2024/2025', max_length=50, verbose_name='Academic Year')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extracurricular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extracurricular.extracurricular')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
            options={
                'verbose_name': 'Student Extracurricular',
                'verbose_name_plural': 'Student Extracurricular Activities',
                'db_table': 'student_extracurricular',
                'ordering': ['extracurricular__extracurricular_name'],
            },
        ),
        migrations.AddIndex(
            model_name='extracurricular',
            index=models.Index(fields=['id', 'slug'], name='extracurric_id_afcce2_idx'),
        ),
        migrations.AddIndex(
            model_name='studentextracurricular',
            index=models.Index(fields=['id'], name='student_ext_id_53cf77_idx'),
        ),
    ]
