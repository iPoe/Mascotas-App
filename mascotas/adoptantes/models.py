from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class adoptante(models.Model):
	correo 					= models.EmailField(verbose_name="email", max_length=255)
	nombre 					= models.CharField(max_length=255)	
	password 				= models.CharField(max_length=255,default='')

	USERNAME_FIELD = 'correo'
	REQUIRED_FIELDS = ['nombre_fund']
#Recuerda hacerle un modelo de perfil para que este pueda ver su información y agregarle una foto


# Create your models here.
