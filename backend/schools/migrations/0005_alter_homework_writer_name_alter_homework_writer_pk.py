# Generated by Django 4.0.1 on 2022-01-22 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_homework_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='writer_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='writer_pk',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
