
# Generated by Django 3.2.8 on 2021-11-03 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_services_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='Like',
        ),
    ]
