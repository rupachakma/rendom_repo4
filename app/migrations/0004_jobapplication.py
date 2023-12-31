# Generated by Django 5.0 on 2023-12-31 17:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_category_alter_skills_title_jobpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('resume', models.FileField(upload_to='resume/')),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jobpost')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
