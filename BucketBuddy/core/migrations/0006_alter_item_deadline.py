# Generated by Django 4.2.1 on 2024-04-27 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_category_item_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 56, 30, 161999)),
        ),
    ]
