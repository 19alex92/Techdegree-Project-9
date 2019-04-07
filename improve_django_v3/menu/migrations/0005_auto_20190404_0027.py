# Generated by Django 2.2 on 2019-04-04 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20190404_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='created_date',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='expiration_date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
