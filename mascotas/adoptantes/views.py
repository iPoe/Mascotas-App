from django.shortcuts import render
from django.views import generic

def pag_registro(request):
	context = {}
	return render(request,'adoptantes/registro.html',context)


def login(request):
	context = {}
	return render(request,'adoptantes/login.html',context)

# Create your views here.
