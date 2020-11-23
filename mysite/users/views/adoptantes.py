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


# def index(request):







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
    #usuario = usuarios.objects.filter(correo = request.user.correo)
    matchs_usuario = Match.objects.get(Idusuario=request.user)
    print(matchs_usuario.IdMascota)
    fotos_slide = Contenido_Multi.objects.filter(id_mascota=matchs_usuario.IdMascota)
    context = {'fotos_slide':fotos_slide}
    #print(request.user.correo)
    return render(request,'adoptantes/slider.html',context)

def vista_main_2(request):
    
    context = {}
    return render(request,'adoptantes/infoFundacion.html',context)