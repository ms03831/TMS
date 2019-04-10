# Generated by Django 2.1.7 on 2019-04-10 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_myuser_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeStart', models.TimeField()),
                ('TimeEnd', models.TimeField()),
                ('Day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Day')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Degree', models.CharField(max_length=100)),
                ('Institution', models.CharField(max_length=100)),
                ('DegreeImage', models.ImageField(upload_to='')),
                ('MyUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.MyUser')),
                ('Qualification', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Qualification')),
            ],
        ),
        migrations.CreateModel(
            name='TutorSubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Board')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Subject')),
                ('Tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tutor')),
            ],
        ),
        migrations.AddField(
            model_name='timming',
            name='Tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tutor'),
        ),
    ]
