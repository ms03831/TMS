# Generated by Django 2.1.7 on 2019-04-17 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190417_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='Highest_Qualification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Qualification'),
        ),
    ]
