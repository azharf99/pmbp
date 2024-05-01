# Generated by Django 5.0.4 on 2024-04-30 18:16

import django.db.models.deletion
import utilities.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_nis', models.CharField(max_length=20, unique=True, verbose_name="Student's Unique Number (NIS)")),
                ('student_nisn', models.CharField(blank=True, max_length=20, null=True, verbose_name="National Student's Unique Number (NISN)")),
                ('student_nik', models.CharField(blank=True, max_length=20, null=True, verbose_name="Student's Family Unique Number (NIK)")),
                ('student_name', models.CharField(max_length=100, verbose_name='Student Name')),
                ('student_class', models.CharField(blank=True, choices=[('X-MIPA-A', 'X-A'), ('X-MIPA-B', 'X-B'), ('X-MIPA-C', 'X-C'), ('X-MIPA-D', 'X-D'), ('X-MIPA-E', 'X-E'), ('X-MIPA-F', 'X-F'), ('X-MIPA-G', 'X-G'), ('X-MIPA-H', 'X-H'), ('XI-MIPA-A', 'XI-A'), ('XI-MIPA-B', 'XI-B'), ('XI-MIPA-C', 'XI-C'), ('XI-MIPA-D', 'XI-D'), ('XI-MIPA-E', 'XI-E'), ('XI-MIPA-F', 'XI-F'), ('XI-MIPA-G', 'XI-G'), ('XI-MIPA-H', 'XI-H'), ('XII-MIPA-A', 'XII-A'), ('XII-MIPA-B', 'XII-B'), ('XII-MIPA-C', 'XII-C'), ('XII-MIPA-D', 'XII-D'), ('XII-MIPA-E', 'XII-E'), ('XII-MIPA-F', 'XII-F'), ('XII-MIPA-G', 'XII-G'), ('XII-MIPA-H', 'XII-H')], max_length=100, null=True, verbose_name="Student's Class")),
                ('student_gender', models.CharField(choices=[('L', 'Male'), ('P', 'Female')], max_length=10, verbose_name="Student's Gender")),
                ('student_address', models.CharField(blank=True, max_length=250, null=True, verbose_name="Student's Address")),
                ('student_birth_place', models.CharField(blank=True, max_length=50, null=True, verbose_name="Student's Birth Place")),
                ('student_birth_date', models.DateField(blank=True, null=True, verbose_name="Student's Birth Date")),
                ('student_email', models.EmailField(blank=True, max_length=50, null=True, verbose_name="Student's Email")),
                ('student_phone', models.CharField(blank=True, max_length=50, null=True, verbose_name="Student's Phone")),
                ('student_status', models.CharField(blank=True, default='Aktif', max_length=50, verbose_name="Student's Status")),
                ('student_photo', utilities.utils.CompressedImageField(blank=True, default='blank-profile.png', help_text='photo format png/jpg', null=True, quality=50, upload_to='student', verbose_name="Student's Photo")),
                ('student_batch', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Student's Batch")),
                ('academic_year', models.CharField(default='2024/2025', max_length=50, verbose_name='Academic Year')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'db_table': 'students',
                'ordering': ['student_class', 'student_name'],
                'indexes': [models.Index(fields=['student_nis', 'id'], name='students_student_cd272c_idx')],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField(default=0, verbose_name='Teacher Unique Number (NIY)')),
                ('teacher_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Teacher Code')),
                ('teacher_name', models.CharField(max_length=100, verbose_name='Teacher Name')),
                ('teacher_gender', models.CharField(choices=[('L', 'Male'), ('P', 'Female')], max_length=1, verbose_name='Teacher Gender')),
                ('teacher_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Teacher Address')),
                ('teacher_job', models.CharField(blank=True, max_length=100, verbose_name='Teacher Job')),
                ('teacher_email', models.EmailField(blank=True, default='smaitalbinaa.ekskul@outlook.com', max_length=254, verbose_name='Teacher Email')),
                ('teacher_phone', models.CharField(blank=True, default=0, max_length=50, verbose_name='Teacher Phone')),
                ('teacher_photo', utilities.utils.CompressedImageField(blank=True, default='blank-profile.png', help_text='photo format png/jpg', null=True, quality=50, upload_to='teacher', verbose_name='Teacher Photo')),
                ('is_active', models.BooleanField(default=True, verbose_name='Teacher Active Status')),
                ('is_online', models.BooleanField(default=False, verbose_name='Teacher Online Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
                'db_table': 'teachers',
                'ordering': ['teacher_name'],
                'indexes': [models.Index(fields=['id'], name='teachers_id_205f85_idx')],
            },
        ),
    ]
