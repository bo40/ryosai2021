# Generated by Django 3.2.5 on 2021-10-28 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ryosai_2021', '0002_auto_20211029_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pro',
            name='image',
        ),
    ]
