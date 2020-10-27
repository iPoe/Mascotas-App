from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


from .forms import CreateUserForm

def pag_registro_adoptante(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form': form}
	return render(request,'adoptantes/registro.html',context)

def pag_registro_fundacion(request):
	context = {}
	return render(request,'adoptantes/registro_fundacion.html',context)


def login_adoptante(request):
	context = {}
	return render(request,'adoptantes/login.html',context)

# Create your views here.
