# Generated by Django 3.2.7 on 2021-12-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_remove_services_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='duration',
            field=models.IntegerField(choices=[(30, 30), (60, 60), (90, 90)], default=30),
        ),
    ]