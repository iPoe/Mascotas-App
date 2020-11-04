from django import forms
from django.contrib.auth.forms import UserCreationForm

from fundacion.models import UsuarioFundacion


class RegistrarFundacionForm(UserCreationForm):

	correo = forms.EmailField(max_length=60,help_text="Obligatorio, Añade una dirreción de correo valida")


	class Meta:
		model = UsuarioFundacion
		fields = ("correo","nombre_fund","info_fundacion","ciudad","password1","password2")

	# def save(self):
	# 	fundacion  = UsuarioFundacion(
	# 			correo = self.validated_data['correo'],
	# 			nombre_fund = self.validated_data['nombre_fund'],
	# 			info_fundacion = self.validated_data['info_fundacion']
	# 		)





