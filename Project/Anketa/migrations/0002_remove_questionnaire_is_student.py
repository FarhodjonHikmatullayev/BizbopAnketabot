# Generated by Django 5.1 on 2024-10-06 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Anketa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='is_student',
        ),
    ]