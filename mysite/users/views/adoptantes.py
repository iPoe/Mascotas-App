from django.contrib.auth import login,authenticate, logout
from django.shortcuts import redirect,render
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, resolve

from ..models import usuarios


from ..models import Mascota
from ..models import Match
from ..models import Contenido_Multi
from ..forms import AdoptSignUpForm,UserloginForm, NuevoMatch
from ..decorators import adop_required


from ..forms import AdoptSignUpForm
#Create password to easy message


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

#Todo-login view para adoptantes
def loginPage(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        user = authenticate(request,username=correo,password=password)
        #print(user.es_fundacion)
        if user is not None:
            login(request,user)
            if user.es_adoptante:
                return redirect('users:main')
            else:
                return redirect('users:agregar')
    context = {}
    return render(request,'adoptantes/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('users:login')




def vista_main_2(request):
    context = {}
    return render(request,'adoptantes/infoFundacion.html',context)

class Catalogo(ListView):

    model = Mascota
    template_name = 'adoptantes/catalogo.html'

    context_object_name = 'mascotas'
    paginate_by = 1

    #def get_context_data(self, *args, **kwargs):
     #   context = super().get_context_data(*args, **kwargs)
      #  context['info'] = Fundacion.objects.filter(usuario=self.request.user)
       # return context

    def get_queryset(self):
        q1 = Mascota.objects.all()
        q2 = Match.objects.filter(Idusuario=self.request.user)
        for i in q2:
            q1 = q1.exclude(id=i.IdMascota.id)
        
        return q1

class CrearMatch(CreateView):
    model = Match
    form_class = NuevoMatch
    template_name = 'adoptantes/match.html'

    def form_valid(self, form):
        form.instance.IdMascota = Mascota.objects.get(id=self.kwargs['pk'])
        form.instance.Idusuario = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('users:main')

class SeleccionarMatch(ListView):

    model = Match
    template_name = 'adoptantes/mis_match.html'
    #queryset = Mascota.objects.filter(idfundacion="2")
    context_object_name = 'mascotas'
    paginate_by = 3

    def get_queryset(self):
        q1 = Mascota.objects.all()
        q2 = Match.objects.filter(Idusuario=self.request.user)
        for i in q2:
            q1 = q1.exclude(id=i.IdMascota.id)
        
        q3 = Mascota.objects.all()
        q1 = q3.difference(q1)
        print(q1)
        return q1

class PerfilMascota(ListView):

    model = Mascota
    template_name = 'adoptantes/perfil.html'
    #queryset = Mascota.objects.filter(idfundacion="2")
    context_object_name = 'multimedia'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['info'] = Mascota.objects.filter(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Contenido_Multi.objects.filter(id_mascota=self.kwargs['pk'])
        