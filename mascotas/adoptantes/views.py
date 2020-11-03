from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login


from .forms import CreateUserForm

def pag_registro_adoptante(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form': form}
	return render(request,'adoptantes/registro.html',context)



def login_adoptante(request):
	context = {}
	# if request.method == 'POST':
	# 	request.POST.get('username')
	# 	request.POST.get('password')

	return render(request,'adoptantes/login_1.html',context)

def vista_main(request):
	context = {}
	return render(request,'adoptantes/main.html',context)

# Create your views here.
