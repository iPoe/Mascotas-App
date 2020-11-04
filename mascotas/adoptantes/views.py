from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import  messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from . import forms

class vista_registro_adoptante(FormView):
	#form = CreateUserForm()
	form_class = forms.RegistrarAdoptante
	template_name = 'adoptantes/registro.html'
	success_url = reverse_lazy('adoptantes:main')
	fail_url = reverse_lazy('adoptantes:registro')

	def form_valid(self,form):
		if form.cleaned_data['password'] == form.cleaned_data['password2']:
			user = form.save(commit=False)
			user.save()
			login(self.request,user)
			if user is not None:
				return HttpResponseRedirect(self.success_url)
			return super().form_valid(form)
		else:
			messages.info(self.request,'Mistakes were made')
			return HttpResponseRedirect(self.fail_url)

class LoginView(FormView):
    """login view"""

    form_class = forms.LoginAdoptante
    success_url = reverse_lazy('adoptantes:main')
    template_name = 'adoptantes/login_1.html'

    def form_valid(self, form):
        """ process user login"""
        correo = form.cleaned_data['correo']
        password = form.cleaned_data['password']

        user = authenticate(username=correo,
                            password=password)
        print(user,correo,password)

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect(reverse_lazy('adoptantes:login'))



# def login_usuario(request):
	
# 	if request.method == 'POST':
# 		username = request.POST.get('username') #CHEQUEAR SI ES ADOPTANTE O FUNDACIÓN
# 		password = request.POST.get('password')
# 		user = authenticate(request,username=username,password=password)

# 		if user is not None:
# 			login(request,user)
# 			return redirect('main')
# 		else:
# 			messages.info(request,'Usuario o contraseña no validos')

# 	context = {}
# 	return render(request,'adoptantes/login_1.html',context)

def vista_main(request):
	context = {}
	return render(request,'adoptantes/main.html',context)

# Create your views here.
