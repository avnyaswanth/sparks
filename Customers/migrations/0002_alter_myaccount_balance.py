# Generated by Django 3.2.5 on 2021-07-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myaccount',
            name='Balance',
            field=models.PositiveIntegerField(default=10000000),
        ),
    ]