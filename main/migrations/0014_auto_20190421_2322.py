# Generated by Django 2.1.7 on 2019-04-21 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='receivingUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='messages',
            name='sendingUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sent_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
