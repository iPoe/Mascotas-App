# Generated by Django 3.2 on 2020-11-08 15:24

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nombre', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('es_adoptante', models.BooleanField(default=False, verbose_name='adoptante estado')),
                ('es_fundacion', models.BooleanField(default=False, verbose_name='fundacion estado')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fundacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fund', models.CharField(max_length=255, unique=True)),
                ('info_fundacion', models.CharField(max_length=255)),
                ('ciudad', models.CharField(blank=True, choices=[('Palmira', 'Palmira'), ('Cali', 'Cali'), ('Candelaria', 'Candelaria')], max_length=10)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdAdoptante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('IdFundacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.fundacion')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('Descripcion', models.CharField(max_length=255)),
                ('Tipo_Mascota', models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato'), ('Otro', 'Otro')], max_length=10)),
                ('Edad', models.IntegerField()),
                ('genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1)),
                ('Estado_esterilzacion', models.CharField(choices=[('No_esterilizado', 'No Esterilizado'), ('Esterilizado', 'Esterilizado')], max_length=20)),
                ('Estado_salud', models.CharField(max_length=255)),
                ('idfundacion', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.fundacion')),
            ],
        ),
        migrations.CreateModel(
            name='Contenido_Multi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contenido', models.CharField(choices=[('Foto', 'Foto'), ('Video', 'Video')], max_length=10)),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to='FOTOS')),
                ('id_mascota', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.mascota')),
            ],
        ),
    ]
