# Generated by Django 4.2.1 on 2023-05-06 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='data_added',
        ),
    ]
