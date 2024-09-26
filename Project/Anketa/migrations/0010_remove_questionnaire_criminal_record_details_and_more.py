# Generated by Django 5.1 on 2024-09-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anketa', '0009_questionnaire_previous_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='criminal_record_details',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='has_criminal_record',
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='gender',
            field=models.CharField(max_length=10, verbose_name='Jinsi'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='languages',
            field=models.TextField(blank=True, verbose_name='Qaysi tillarni bilasiz? va qay darajada'),
        ),
    ]