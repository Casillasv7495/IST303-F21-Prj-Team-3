# Generated by Django 3.2.7 on 2021-09-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='Like',
            field=models.BooleanField(default=True),
        ),
    ]