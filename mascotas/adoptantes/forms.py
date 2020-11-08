from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from adoptantes.models import adoptante



class RegistrarAdoptante(forms.ModelForm):
	"""Formulario para registrar adoptantes"""
	#correo = forms.EmailField(max_length=60,help_text="Obligatorio, Añade una dirreción de correo valida")
	password = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = adoptante
		fields = ('correo','nombre','password')

class LoginAdoptante(forms.ModelForm):
	"""Form para el login del adoptante"""
	model = adoptante
	correo = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())
	# class Meta:
	# 	model = adoptante
	# 	fields = ['correo','password']





