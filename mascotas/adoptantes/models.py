from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """custom user manager class"""
    use_in_migration = True

    def _create_user(self, email, password,name, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class adoptante(AbstractBaseUser):
	correo 					= models.EmailField(verbose_name="email", max_length=255,unique=True)
	nombre 					= models.CharField(max_length=255)
	is_active 				= models.BooleanField(_('is_active'), default=True)
	#password 				= models.CharField(max_length=255,default='')

	USERNAME_FIELD = 'correo'
	REQUIRED_FIELDS = ['nombre']
	objects = CustomUserManager()
	def __str__(self):
		return self.correo
	


#Recuerda hacerle un modelo de perfil para que este pueda ver su información y agregarle una foto


# Create your models here.
