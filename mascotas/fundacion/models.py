from django.db import models
from django.contrib.auth.models import AbstractBaseUser





class UsuarioFundacion(AbstractBaseUser):
	correo 					= models.EmailField(verbose_name="email", max_length=255, unique=True)
	nombre_fund 			= models.CharField(max_length=255, unique=True)
	info_fundacion 			= models.CharField(max_length=255)
	opciones_ciudades		= models.TextChoices('City','Palmira Cali Candelaria')
	ciudad 					= models.CharField(blank=True,choices=opciones_ciudades.choices,max_length=10)
	password 				= models.CharField(max_length=255,default='')

	USERNAME_FIELD = 'correo'
	REQUIRED_FIELDS = ['nombre_fund']

class mascota(models.Model):
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
	Estado_esterilzacion = models.CharField(max_length=255)
	Estado_salud = models.CharField(max_length=255)

	#objects = MyAccountManager()

# Create your models here.
