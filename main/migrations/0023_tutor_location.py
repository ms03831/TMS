# Generated by Django 2.1.7 on 2019-05-05 07:14

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_messages_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='12,12', max_length=63),
            preserve_default=False,
        ),
    ]