# Generated by Django 5.1.2 on 2024-10-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='emp_email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
