# Generated by Django 4.0.4 on 2022-09-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_accounts_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='Landlords'),
        ),
    ]
