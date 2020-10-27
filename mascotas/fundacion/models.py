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

	#objects = MyAccountManager()

# Create your models here.
