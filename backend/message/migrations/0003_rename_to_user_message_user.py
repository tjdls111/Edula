# Generated by Django 4.0.1 on 2022-02-15 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_message_send'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='to_user',
            new_name='user',
        ),
    ]
