from django.urls import include, path
from users.views import adoptantes
from users.views import fundacion
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'



urlpatterns = [
	path('reg/', adoptantes.AdoptSignUpView.as_view(),name="registro"),
	path('main/',adoptantes.vista_main,name="main"),
	

	path('agregar/', fundacion.AgregarMascota.as_view(),name="agregar"),
	#path('editar/', fundacion.editar,name="editar"),
	path('eliminar/<int:pk>', fundacion.EliminarMascota.as_view(),name="eliminar"),
	path('eliminar/', fundacion.SeleccionarMascotaEliminar.as_view(),name="sel_eliminar"),

	path('seleccionar/', fundacion.SeleccionarMascota.as_view(),name="seleccionar"),
	path('editar/<int:pk>', fundacion.EditarMascota.as_view(), name='editar'),

	path('agregar_multimedia/<int:pk>', fundacion.AgregarMulti.as_view(), name='agregar_multi'),
	path('multimedia/<int:pk>', fundacion.VerMultimedia.as_view(), name='multimedia')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)