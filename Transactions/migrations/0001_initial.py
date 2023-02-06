# Generated by Django 4.0.4 on 2022-08-30 21:06

import Transactions.models
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('TransactionType', models.CharField(default='CustomerPayBillOnline', max_length=15)),
                ('Amount', models.FloatField()),
                ('PartyA', models.IntegerField(validators=[Transactions.models.phone_validator])),
                ('PartyB', models.IntegerField(default=174379)),
                ('PhoneNumber', models.IntegerField(validators=[Transactions.models.phone_validator])),
                ('AccountReference', models.CharField(max_length=20)),
                ('TransactionDesc', models.CharField(default='Rent Payments', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('Transaction_id', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('amount', models.FloatField()),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_number', models.CharField(max_length=15)),
                ('receiver_number', models.CharField(max_length=15)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]