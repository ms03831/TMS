# Generated by Django 2.1.7 on 2019-04-16 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190416_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='board',
            new_name='Board',
        ),
    ]
