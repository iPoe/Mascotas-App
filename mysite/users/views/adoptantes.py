from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect,render
from django.views.generic import CreateView


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from ..models import usuarios
from ..models import Mascota
from ..models import Match
from ..models import Contenido_Multi
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


@login_required
@adop_required
def vista_main(request):
    mascotas = Mascota.objects.all()
    fotos_slide = Contenido_Multi.objects.filter(id_mascota__in=mascotas)
    context = {'fotos_slide':fotos_slide}
    ##What to do to capture the pet and added to likes
    #when button is clicked
    if request.method == 'POST':
        print("Script Working....")

    return render(request,'adoptantes/catálogo.html',context)

#@login_required
#def perfil(request):

#    nombre = usuarios.get(correo=request.user)
#    correo = usuarios.get(nombre=request.user)
#    context = {nombre, correo}
#    return render(request,'adoptantes/perfil.html', context)



def vista_main_2(request):
    
    context = {}
    return render(request,'adoptantes/infoFundacion.html',context)