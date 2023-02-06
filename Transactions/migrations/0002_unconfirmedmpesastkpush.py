# Generated by Django 4.0.4 on 2022-10-20 09:17

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnconfirmedMpesaStkPush',
            fields=[
                ('id', models.CharField(default=uuid.uuid1, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('MerchantRequestID', models.CharField(max_length=100)),
                ('CheckoutRequestID', models.CharField(max_length=100)),
                ('ResponseDescription', models.CharField(max_length=100)),
                ('CustomerMessage', models.CharField(max_length=100)),
                ('ResponseCode', models.IntegerField()),
                ('amount', models.FloatField()),
                ('Timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('PAID', 'PAID'), ('CANCELLED', 'CANCELLED'), ('ERROR', 'ERROR'), ('IN_PROGRES', 'IN_PROGRES')], default='IN_PROGRES', max_length=100)),
            ],
        ),
    ]
