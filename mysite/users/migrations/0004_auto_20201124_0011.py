# Generated by Django 3.2 on 2020-11-24 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201109_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='ciudad',
            field=models.CharField(blank=True, choices=[('Palmira', 'Palmira'), ('Cali', 'Cali'), ('Candelaria', 'Candelaria')], max_length=10),
        ),
        migrations.AddField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(null=True, upload_to='Mascotas/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='idfundacion',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.fundacion'),
        ),
    ]