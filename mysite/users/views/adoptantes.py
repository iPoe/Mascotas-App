from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url
from ..models import usuarios
from ..forms import AdoptSignUpForm,UserloginForm


class AdoptSignUpView(CreateView):
    model = usuarios
    form_class = AdoptSignUpForm
    template_name = 'adoptantes/registro_adop.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'adoptante'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:main')


#Todo-login view para adoptantes
def loginPage(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        user = authenticate(request,username=correo,password=password)
        print(user.es_fundacion)
        if user is not None:
            login(request,user)
            return redirect('users:main')
    context = {}
    return render(request,'adoptantes/login.html',context)


#@login_required(login_url='users:registro')
def vista_main(request):
    context = {}
    return render(request,'adoptantes/misMatch.html',context)