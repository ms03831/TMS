# Generated by Django 2.1.7 on 2019-05-13 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_messages_conversation'),
    ]

    operations = [
        migrations.AddField(
            model_name='contracts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]