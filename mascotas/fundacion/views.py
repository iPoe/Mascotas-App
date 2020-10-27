from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate
from fundacion.forms import RegistrarFundacionForm



# Create your views here.

def registro(request):
	form = RegistrarFundacionForm()

	if request.method == 'POST':
		form = RegistrarFundacionForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form': form}
	return render(request,'fundacion/registro.html',context)