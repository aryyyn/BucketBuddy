# Generated by Django 4.2.1 on 2024-04-27 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='Deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 39, 41, 737982)),
        ),
    ]
