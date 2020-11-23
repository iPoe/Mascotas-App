from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from ..models import usuarios
<<<<<<< HEAD
from ..models import Mascota
from ..models import Match
from ..models import Contenido_Multi
from ..forms import AdoptSignUpForm,UserloginForm
from ..decorators import adop_required

=======
from ..forms import AdoptSignUpForm
>>>>>>> parent of 4c4937d... Merge branch 'main' of https://github.com/iPoe/Mascotas-App into main


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
<<<<<<< HEAD
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
    
=======
>>>>>>> parent of 4c4937d... Merge branch 'main' of https://github.com/iPoe/Mascotas-App into main
    context = {}
    return render(request,'adoptantes/main.html',context)