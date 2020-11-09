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

class AdoptloginForm(forms.ModelForm):
    model = usuarios
    correo = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


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
        usuario = usuarios(correo = self.validated_data['correo'],password = self.validated_data['password1'])
        usuario_fund = Fundacion(
            correo = self.validated_data['correo'],
          nombre_fund = self.validated_data['nombre_fund'],
          info_fundacion = self.validated_data['info_fundacion'],
          ciudad = self.validated_data['ciudad']
            )
        usuario.es_fundacion=True
        usuario.save()
        usuario_fund.save()
        print(usuario_fund)
        return usuario 
        

