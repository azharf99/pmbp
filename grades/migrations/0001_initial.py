# Generated by Django 5.0.4 on 2024-04-30 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extracurricular', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=3, verbose_name='Grade')),
                ('academic_year', models.CharField(default='2024/2025', max_length=50, verbose_name='Academic Year')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extracurricular.studentextracurricular', verbose_name='Student Name')),
            ],
            options={
                'verbose_name': 'Grade',
                'verbose_name_plural': 'Grades',
                'db_table': 'grades',
                'ordering': ['student'],
                'indexes': [models.Index(fields=['id'], name='grades_id_3fb9b3_idx')],
            },
        ),
    ]
