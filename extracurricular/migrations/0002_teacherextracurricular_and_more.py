# Generated by Django 5.0.4 on 2024-05-03 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extracurricular', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherExtracurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(default='2024/2025', max_length=50, verbose_name='Academic Year')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Teacher Extracurricular',
                'verbose_name_plural': 'Teacher Extracurricular Activities',
                'db_table': 'extracurricular_teachers',
                'ordering': ['extracurricular__extracurricular_name'],
            },
        ),
        migrations.RenameIndex(
            model_name='studentextracurricular',
            new_name='extracurric_id_ca3d51_idx',
            old_name='student_ext_id_53cf77_idx',
        ),
        migrations.RemoveField(
            model_name='extracurricular',
            name='extracurricular_teacher',
        ),
        migrations.AlterModelTable(
            name='studentextracurricular',
            table='extracurricular_students',
        ),
        migrations.AddField(
            model_name='teacherextracurricular',
            name='extracurricular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extracurricular.extracurricular'),
        ),
        migrations.AddField(
            model_name='teacherextracurricular',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
        migrations.AddIndex(
            model_name='teacherextracurricular',
            index=models.Index(fields=['id'], name='extracurric_id_d77519_idx'),
        ),
    ]