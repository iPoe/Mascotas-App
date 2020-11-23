from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import usuarios,Fundacion, Mascota, Contenido_Multi

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

class AgregarMascota(forms.ModelForm):
    class Meta():
        model = Mascota
        exclude = ("idfundacion",)
        fields = ("foto","Nombre","Descripcion","Tipo_Mascota","Edad","genero","Estado_salud","Estado_esterilzacion","ciudad")
        
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'w3-input w3-border w3-light-grey'}),
            'Descripcion': forms.TextInput(attrs={'class': 'w3-input w3-border w3-light-grey'}),
            'Tipo_Mascota': forms.Select(attrs={'class': 'w3-input w3-border w3-light-grey'}),
            'Edad': forms.NumberInput(attrs={'class': 'w3-input w3-border w3-light-grey'}),
            'genero': forms.Select(attrs={'class': 'w3-input w3-border w3-light-grey'}),
            'Estado_salud': forms.TextInput(attrs={'class': 'w3-input w3-border w3-light-grey'}),
            'Estado_esterilzacion': forms.Select(attrs={'class': 'w3-input w3-border w3-light-grey'}),
            'ciudad': forms.Select(attrs={'class': 'w3-input w3-border w3-light-grey'})
        }
    
class AgregarMultimedia(forms.ModelForm):
    class Meta():
        model = Contenido_Multi
        exclude = ("id_mascota",)
        fields = ("tipo_contenido","titulo","descripcion","foto")
        
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'w3-input w3-border w3-light-grey'}),
            'titulo': forms.TextInput(attrs={'class': 'w3-input w3-border w3-light-grey'}),
            'tipo_contenido': forms.Select(attrs={'class': 'w3-input w3-border w3-light-grey'}),
        }       

