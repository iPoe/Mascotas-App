# Generated by Django 3.2 on 2020-11-03 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundacion', '0008_auto_20201103_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido_multi',
            name='foto',
            field=models.ImageField(upload_to='FOTOS'),
        ),
    ]