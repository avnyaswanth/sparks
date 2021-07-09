# Generated by Django 3.2.5 on 2021-07-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomersDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=100)),
                ('AccountNumber', models.BigIntegerField(max_length=17)),
                ('CustomerMail', models.EmailField(max_length=100)),
                ('Balance', models.PositiveIntegerField(default=10000)),
            ],
        ),
        migrations.CreateModel(
            name='MyAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MyName', models.CharField(max_length=100)),
                ('AccountNumber', models.BigIntegerField(max_length=17)),
                ('MyMail', models.EmailField(max_length=100)),
                ('Balance', models.PositiveIntegerField(default=100000)),
            ],
        ),
    ]
