# Generated by Django 3.2 on 2020-11-04 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptantes', '0002_auto_20201104_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptante',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
    ]