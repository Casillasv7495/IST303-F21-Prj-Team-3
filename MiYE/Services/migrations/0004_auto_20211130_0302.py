# Generated by Django 3.2.7 on 2021-11-30 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_remove_services_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='services',
            old_name='Service',
            new_name='name',
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.types')),
            ],
        ),
        migrations.AddField(
            model_name='services',
            name='options',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Services.options'),
        ),
        migrations.AddField(
            model_name='services',
            name='types',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Services.types'),
        ),
    ]
