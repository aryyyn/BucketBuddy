# Generated by Django 4.2.1 on 2024-04-27 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_user_alter_item_deadline_alter_item_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Status',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='item',
            name='Deadline',
        ),
        migrations.AddField(
            model_name='item',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 11, 56, 20, 646812)),
        ),
    ]
