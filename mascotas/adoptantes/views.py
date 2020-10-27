from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

def pag_registro(request):
	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form': form}
	return render(request,'adoptantes/registro.html',context)


def login(request):
	context = {}
	return render(request,'adoptantes/login.html',context)

# Create your views here.
