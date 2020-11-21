from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import usuarios,Fundacion

class AdoptSignUpForm(UserCreationForm):
    correo = forms.EmailField(label="Correo electrónico")

    class Meta(UserCreationForm.Meta):
        model = usuarios
        fields = ["correo","nombre", "password1", "password2"]
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.es_adoptante = True
        user.save()
        return user

class UserloginForm(forms.ModelForm):
    correo = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = usuarios
        fields = ["correo","password"]


class FundacionSignUpForm(UserCreationForm):
    correo = forms.EmailField(label="Correo")
    nombre_fund = forms.CharField(max_length=20)
    info_fundacion = forms.CharField(max_length=50)
    list_ciudades = ((1,'Cali'),(2,'Palmira'))
    ciudad = forms.ChoiceField(choices=list_ciudades)
    class Meta(UserCreationForm.Meta):
        model = usuarios
        fields = ("correo","nombre_fund","info_fundacion","ciudad","password1","password2")
    def save(self):
        user = super().save(commit=False)
        user.es_fundacion=True
        user.save()        
        usuario_fund = Fundacion(
            usuario = user,
          nombre_fund = self.cleaned_data['nombre_fund'],
          info_fundacion = self.cleaned_data['info_fundacion'],
          ciudad = self.cleaned_data['ciudad']
            )
        # usuario.es_fundacion=True
        # usuario.save()
        usuario_fund.save()
        # print(usuario_fund)
        # return usuario 
        return user

