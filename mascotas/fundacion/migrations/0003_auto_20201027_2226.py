# Generated by Django 3.2 on 2020-10-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundacion', '0002_auto_20201027_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariofundacion',
            name='correo',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='usuariofundacion',
            name='nombre_fund',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
