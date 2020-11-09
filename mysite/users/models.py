from django.db import models

from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, correo, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not correo:
            raise ValueError(_('The Email must be set'))
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,correo, password,username=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """        
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(correo, password, **extra_fields)


# Create your models here.


class usuarios(AbstractUser):
    username = None
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(_('email address'), unique=True)
    es_adoptante = models.BooleanField('adoptante estado', default=False)
    es_fundacion = models.BooleanField('fundacion estado', default=False) 


    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    objects = CustomUserManager()

    def __str__(self):
        return self.correo



class Fundacion(models.Model):
	usuario 				= models.OneToOneField(usuarios, on_delete=models.CASCADE)
	nombre_fund 			= models.CharField(max_length=255, unique=True)
	info_fundacion 			= models.CharField(max_length=255)
	opciones_ciudades		= models.TextChoices('City','Palmira Cali Candelaria')
	ciudad 					= models.CharField(blank=True,choices=opciones_ciudades.choices,max_length=10)


	def __str__(self):
		return self.nombre_fund

class Mascota(models.Model):
	Nombre = models.CharField(max_length=20)
	Descripcion = models.CharField(max_length=255)
	opciones_tipo = models.TextChoices('Tipo','Perro Gato Otro')
	Tipo_Mascota = models.CharField(choices=opciones_tipo.choices,max_length=10)
	Edad = models.IntegerField()
	opciones_genero = (
			('F','Femenino'),
			('M','Masculino')
		)
	genero = models.CharField(max_length=1,choices=opciones_genero)
	opciones_esterilizacion = models.TextChoices('Estado','No_esterilizado Esterilizado')
	Estado_esterilzacion = models.CharField(choices=opciones_esterilizacion.choices, max_length=20)
	Estado_salud = models.CharField(max_length=255)
	idfundacion = models.ForeignKey(Fundacion,on_delete=models.CASCADE,default=None)

class Match(models.Model):
	Idusuario = models.ForeignKey(usuarios,on_delete=models.CASCADE,default=None)
	IdMascota = models.ForeignKey(Mascota,on_delete=models.CASCADE,default=None)

class Contenido_Multi(models.Model):
	id_mascota = models.ForeignKey(Mascota,on_delete=models.CASCADE,default=None)
	opciones_tipo = models.TextChoices('Tipo','Foto Video')
	tipo_contenido = models.CharField(choices=opciones_tipo.choices,max_length=10)
	titulo = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=255)
	foto = models.ImageField(upload_to= 'FOTOS')
	def __str__(self):
		return self.id_mascota


# Create your models here.
