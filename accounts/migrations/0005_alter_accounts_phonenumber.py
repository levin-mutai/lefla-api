# Generated by Django 4.0.4 on 2022-06-12 08:32

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_accounts_is_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]
