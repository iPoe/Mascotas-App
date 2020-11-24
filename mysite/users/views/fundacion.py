from django.contrib.auth import login,authenticate
from django.shortcuts import redirect,render
from django.urls import reverse_lazy, resolve
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404
from ..models import usuarios, Fundacion, Mascota, Match, Contenido_Multi
from ..forms import AdoptSignUpForm, AgregarMascota, AgregarMultimedia,FundacionSignUpForm

from django.contrib.messages.views import SuccessMessageMixin



class FundtSignUpView(CreateView):
    model = usuarios
    form_class = FundacionSignUpForm
    template_name = 'fundaciones/registro_f.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'fundacion'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #print(user)
        login(self.request, user)
        return redirect('users:main')
"""
def agregar(request):

	info = Fundacion.objects.filter(nombre_fund="2")
	if request.method == 'POST':
		form = AgregarMascota(request.POST or None, request.FILES or None)
		
		print(form.errors)
		if form.is_valid():
			post = form.save(commit=False)
			post.idfundacion = info[0]
			post.save()

	form = AgregarMascota()
	context ={'info':info,'form':form}
	return render(request,'fundacion/agregar.html',context) 



def editar(request,id_mascota):
	info = Fundacion.objects.filter(nombre_fund="2")
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.Nombre = request.POST.get('Nombre')
		mascota.Descripcion = request.POST.get('Descripcion')
		mascota.Edad = request.POST.get('Edad')
		mascota.genero = request.POST.get('genero')
		mascota.Tipo_Mascota = request.POST.get('Tipo_Mascota')
		mascota.Estado_esterilzacion = request.POST.get('Estado_esterilzacion')
		mascota.Estado_salud = request.POST.get('Estado_salud')
		mascota.ciudad = request.POST.get('ciudad')
		mascota.foto = request.FILES.get('foto')
		mascota.save()

	form = AgregarMascota(initial={"Nombre":mascota.Nombre,
									"Descripcion":mascota.Descripcion,
									"Edad":mascota.Edad,
									"genero":mascota.genero,
									"Tipo_Mascota":mascota.Tipo_Mascota,
									"Estado_esterilzacion":mascota.Estado_esterilzacion,
									"Estado_salud":mascota.Estado_salud,
									"ciudad":mascota.ciudad,
									"foto":mascota.foto,
									"idfundacion":info[0]})
	context ={'info':info,'form':form}
	return render(request,'fundacion/editar.html',context)


def eliminar_final(request,id_mascota):
	info = Fundacion.objects.filter(nombre_fund="2")
	if request.method == 'POST':

		Mascota.objects.filter(id=id_mascota).delete()
		mascotas = Mascota.objects.filter(idfundacion="2")
		return redirect('users:eliminar')

	context ={'info':info, 'mascotas':Mascota.objects.filter(id=id_mascota)}
	return render(request,'fundacion/eliminar_final.html',context)

def eliminar(request):
	info = Fundacion.objects.filter(nombre_fund="2")
	mascotas = Mascota.objects.filter(idfundacion="2")
	if request.method == 'POST':
		mascota_id = request.POST.get('id')
		return redirect('eliminar_final',mascota_id)
	context ={'info':info, 'mascotas':mascotas}
	return render(request,'fundacion/eliminar.html',context)
	

def seleccionar(request):
	info = Fundacion.objects.filter(nombre_fund="2")
	mascotas = Mascota.objects.filter(idfundacion="2")
	if request.method == 'POST':
		mascota_id = request.POST.get('id')
		return redirect('editar',mascota_id)
	context ={'info':info, 'mascotas':mascotas}
	return render(request,'fundacion/seleccionar.html',context)
"""
# Clases 

class EditarMascota(SuccessMessageMixin, UpdateView):
	model = Mascota
	form_class = AgregarMascota
	template_name = 'fundacion/editar.html'
	context_object_name = 'mascotas'
	success_message = "Mascota Editada Correctamente!"

	def get_queryset(self):
		return Mascota.objects.filter(id=self.kwargs['pk'])
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['info'] = Fundacion.objects.filter(usuario=self.request.user)
		return context

    
	success_url = reverse_lazy('users:seleccionar')

class EliminarMascota(SuccessMessageMixin, DeleteView):
	model = Mascota
	template_name = 'fundacion/eliminar_final.html'
	context_object_name = 'mascotas'
	success_message = "Mascota Eliminada Correctamente!"

	


	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['info'] = Fundacion.objects.filter(usuario=self.request.user)
		return context

	success_url = reverse_lazy('users:sel_eliminar')

class SeleccionarMascotaEliminar(ListView):

	model = Mascota
	template_name = 'fundacion/eliminar.html'
	#queryset = Mascota.objects.filter(idfundacion="2")
	context_object_name = 'mascotas'
	paginate_by = 3

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['info'] = Fundacion.objects.filter(usuario=self.request.user)
		return context
	def get_query_set(self):		
		return Mascota.objects.filter(idfundacion=Fundacion.objects.get(usuario=self.request.user))


class SeleccionarMascota(ListView):

	model = Mascota
	template_name = 'fundacion/seleccionar.html'
	#queryset = Mascota.objects.filter(idfundacion="2")
	context_object_name = 'mascotas'
	paginate_by = 3

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['info'] = Fundacion.objects.filter(usuario=self.request.user)
		return context
	def get_query_set(self):		
		return Mascota.objects.filter(idfundacion=Fundacion.objects.get(usuario=self.request.user))


"""
class SeleccionarMascota(ListView):

	model = Mascota
	template_name = 'fundacion/seleccionar.html'
	#queryset = Mascota.objects.filter(idfundacion=Fundacion.objects.get(usuario=self.request.user))
	context_object_name = 'mascotas'
	paginate_by = 1

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['info'] = Fundacion.objects.filter(usuario=self.request.user)
		return context
	def get_query_set(self):		
		return Mascota.objects.filter(idfundacion=Fundacion.objects.get(usuario=self.request.user))
"""
class AgregarMascota(SuccessMessageMixin, CreateView):
	model = Mascota
	form_class = AgregarMascota
	template_name = 'fundacion/agregar.html'
	context_object_name = 'mascotas'
	success_message = "Mascota Agregada Correctamente!"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['info'] = Fundacion.objects.filter(usuario=self.request.user)
		return context

	def form_valid(self, form):
		form.instance.idfundacion = Fundacion.objects.get(usuario=self.request.user)
		return super(AgregarMascota, self).form_valid(form)

	success_url = reverse_lazy('users:agregar')

class AgregarMulti(SuccessMessageMixin, CreateView):
	model = Contenido_Multi
	form_class = AgregarMultimedia
	template_name = 'fundacion/agregar_multi.html'
	context_object_name = 'multimedia'
	success_message = "Contenido Multimedia Agregado Correctamente!"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['info'] = Fundacion.objects.filter(usuario=self.request.user)
		return context

	def form_valid(self, form):
		form.instance.id_mascota = Mascota.objects.get(id=self.kwargs['pk'])
		return super().form_valid(form)

	def get_success_url(self):
		id_mascota = self.kwargs['pk']
		return reverse_lazy('users:editar', kwargs={'pk': id_mascota})

class VerMultimedia(ListView):

	model = Contenido_Multi
	template_name = 'fundacion/multimedia.html'
	context_object_name = 'multimedia'
	paginate_by = 1

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['info'] = Fundacion.objects.filter(nombre_fund="2")
		context['mascota'] = Mascota.objects.get(id=self.kwargs['pk'])
		return context
	def get_queryset(self):
		return Contenido_Multi.objects.filter(id_mascota=self.kwargs['pk'])
	


