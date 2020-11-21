from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect,render
from django.views.generic import CreateView


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from ..models import usuarios
from ..forms import AdoptSignUpForm,UserloginForm
from ..decorators import adop_required

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
            if user.es_adoptante:
                return redirect('users:main')
            else:
                return redirect('users:main2')
    context = {}
    return render(request,'adoptantes/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('users:login')


#@login_required(login_url='users:registro')
@login_required
@adop_required
def vista_main(request):
    context = {}
    return render(request,'adoptantes/misMatch.html',context)

def vista_main_2(request):
    context = {}
    return render(request,'adoptantes/infoFundacion.html',context)