from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from adoptantes.models import adoptante

class AdoptantesBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        correo = kwargs['username']
        password = kwargs['password']
        try:
            Usuario_adop = adoptante.objects.get(correo=correo,password=password)
            if Usuario_adop is not None:
                return Usuario_adop
        except Usuario_adop.DoesNotExist:
            return None