from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='/media/fotos')





class UsuarioFundacion(AbstractBaseUser):
	ID_Fundacion 			= models.AutoField(primary_key=True,default=None)
	correo 					= models.EmailField(verbose_name="email", max_length=255)
	nombre_fund 			= models.CharField(max_length=255, unique=True)
	info_fundacion 			= models.CharField(max_length=255)
	opciones_ciudades		= models.TextChoices('City','Palmira Cali Candelaria')
	ciudad 					= models.CharField(blank=True,choices=opciones_ciudades.choices,max_length=10)
	password 				= models.CharField(max_length=255,default='')

	USERNAME_FIELD = 'correo'
	REQUIRED_FIELDS = ['nombre_fund']

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
	idfundacion = models.ForeignKey(UsuarioFundacion,on_delete=models.CASCADE,default=None)
	#USERNAME_FIELD = 'Nombre'

class Contenido_Multi(models.Model):
	id_mascota = models.ForeignKey(Mascota,on_delete=models.CASCADE,default=None)
	opciones_tipo = models.TextChoices('Tipo','Foto Video')
	tipo_contenido = models.CharField(choices=opciones_tipo.choices,max_length=10)
	titulo = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=255)
	foto = models.ImageField(upload_to= 'FOTOS')



	

# Create your models here.
