# Generated by Django 3.2.9 on 2021-11-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0007_alter_run_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='start_time',
            field=models.DateTimeField(verbose_name='date started'),
        ),
    ]
