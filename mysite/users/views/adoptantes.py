from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from ..models import usuarios

from ..models import Mascota
from ..models import Match
from ..models import Contenido_Multi
from ..forms import AdoptSignUpForm,UserloginForm
from ..decorators import adop_required


from ..forms import AdoptSignUpForm


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
        #print(user)
        login(self.request, user)
        return redirect('users:main')


#Todo-login view para adoptantes


@login_required(login_url='users:registro')
def vista_main(request):

    mascotas = Mascota.objects.all()
    fotos_slide = Contenido_Multi.objects.filter(id_mascota__in=mascotas)

    #usuario = usuarios.objects.filter(correo = request.user.correo)
    matchs_usuario = Match.objects.get(Idusuario=request.user)
    print(matchs_usuario.IdMascota)
    fotos_slide = Contenido_Multi.objects.filter(id_mascota=matchs_usuario.IdMascota)

    context = {'fotos_slide':fotos_slide}
    #print(request.user.correo)
    return render(request,'adoptantes/slider.html',context)

#@login_required
#def perfil(request):

#    nombre = usuarios.get(correo=request.user)
#    correo = usuarios.get(nombre=request.user)
#    context = {nombre, correo}
#    return render(request,'adoptantes/perfil.html', context)



def vista_main_2(request):

    context = {}
    return render(request,'adoptantes/main.html',context)