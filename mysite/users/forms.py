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

    class Meta(UserCreationForm.Meta):
        model = Fundacion
        fields = ("correo","nombre_fund","info_fundacion","ciudad","password1","password2")
        

