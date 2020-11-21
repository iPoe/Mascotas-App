# Generated by Django 3.2 on 2020-11-09 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usuarios_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='IdAdoptante',
        ),
        migrations.RemoveField(
            model_name='match',
            name='IdFundacion',
        ),
        migrations.AddField(
            model_name='match',
            name='IdMascota',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.mascota'),
        ),
        migrations.AddField(
            model_name='match',
            name='Idusuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]