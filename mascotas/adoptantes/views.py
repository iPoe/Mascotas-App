from django.shortcuts import render
from django.views import generic

def pag_registro(request):
	context = {}
	return render(request,'adoptantes/registro.html',context)


# Create your views here.
