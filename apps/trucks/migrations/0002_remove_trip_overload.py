# Generated by Django 4.2.1 on 2023-05-12 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='overload',
        ),
    ]