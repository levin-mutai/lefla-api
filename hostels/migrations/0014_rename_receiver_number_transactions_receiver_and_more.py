# Generated by Django 4.0.4 on 2022-11-28 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0013_remove_room_checker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='receiver_number',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='transactions',
            old_name='sender_name',
            new_name='sender',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='sender_number',
        ),
    ]
