from django.test import TestCase
from users.models import usuarios,Match,Mascota,Fundacion
from django.urls import reverse

from django.core.files import File




class Testusuario_adopt_views(TestCase):
	user = None
	def setup(self):
		self.user = usuarios.objects.create(nombre="test",correo="adop5@gmail.com",es_adoptante=True,password="Monster14320")


	def test_login(self):
		data = {
			"correo":"adop5@gmail.com",
			"password":"Monster14320"
		}
		u = usuarios.objects.create(nombre="test",correo="adop5@gmail.com",es_adoptante=True)
		u.set_password("Monster14320")
		u.save()
		logged_in = self.client.login(correo = "adop5@gmail.com",password="Monster14320")
		response = self.client.get("/log/")
		self.assertTemplateUsed(response,"adoptantes/login.html")
		self.assertContains(response,"correo")
		self.assertContains(response,"password")
		response = self.client.post(reverse('users:login'),data=data,follow=True)
		num = usuarios.objects.count()
		self.assertEquals(num,1)

		self.assertRedirects(response,"/main/")

	def test_reg(self):
		data = {
			"correo":"adop5@gmail.com",
			"nombre": "sikas",
			"password1":"Monster14320",
			"password2":"Monster14320"

		}
		response = self.client.get("/reg/")
		response = self.client.post(reverse('users:registro'),data=data,follow=True)
		self.assertEquals(usuarios.objects.count(),1)
		self.assertRedirects(response,"/main/")

	def test_logout(self):
		data = {
			"correo":"adop5@gmail.com",
			"password":"Monster14320"
		}
		u = usuarios.objects.create(nombre="test",correo="adop5@gmail.com",es_adoptante=True)
		u.set_password("Monster14320")
		u.save()
		logged_in = self.client.login(correo = "adop5@gmail.com",password="Monster14320")
		response = self.client.get("/l/",data=data)
		self.assertRedirects(response,"/log/")

	def test_catalogo_match(self):
		data = {
			"correo":"adop5@gmail.com",
			"nombre": "sikas",
			"password1":"Monster14320",
			"password2":"Monster14320"

		}
		uf = usuarios.objects.create(nombre="test",correo="fund5@gmail.com",es_fundacion=True)
		uf.set_password("Monster14320")
		uf.save()
		F = Fundacion(usuario = uf,nombre_fund="fund5",info_fundacion="@FUND5",ciudad="Cali")
		F.save()
		
		m = Mascota(Nombre="ptest",Descripcion="test",Tipo_Mascota="Perro",Edad=1,genero="M",Estado_esterilzacion="Esterilizado",Estado_salud="test",idfundacion=F)
		m.save()
		m2 = Mascota(Nombre="ptest2",Descripcion="test",Tipo_Mascota="Perro",Edad=1,genero="M",Estado_esterilzacion="Esterilizado",Estado_salud="test",idfundacion=F)
		m2.save()


		#response.wsgi_request.user
		
		response = self.client.get("/reg/")
		response = self.client.post(reverse('users:registro'),data=data,follow=True)
		# match_user = Match(Idusuario=response.wsgi_request.user,IdMascota=m)
		# match_user.save()

		
		response = self.client.get("users:main")
		response = self.client.post("/main/{}".format(m.id),data={'Idusuario':response.wsgi_request.user,'IdMascota':m},follow=True)
		self.assertEquals(Match.objects.count(),1)

		response = self.client.get(reverse("users:list_match"),data={'Idusuario':response.wsgi_request.user})
		response = self.client.get("/match/{}".format(m.id))

	def test_fund(self):
		data = {
			"correo":"fund51@gmail.com",
			"nombre_fund": "testfund",
			"info_fundacion":"@fund51",
			"ciudad":1,
			"password1":"Monster14320",
			"password2":"Monster14320"

		}
		response = self.client.get("/regf/")
		response = self.client.post(reverse('users:registroFundacion'),data=data,follow=True)
		self.assertEquals(Fundacion.objects.count(),1)
		# m = Mascota(Nombre="ptest",Descripcion="test",
		# 	Tipo_Mascota="Perro",Edad=1,genero="M",
		# 	Estado_esterilzacion="Esterilizado",Estado_salud="test",idfundacion=Fundacion.objects.get(usuario =response.wsgi_request.user ))
		# m.save()
		file = File(open('/home/leonardo/Downloads/Image Preview.jpg','rb'))
		petdata = {
			"Nombre":"ptest",
			"Descripcion":"ptest",
			"Tipo_Mascota":"Perro",
			"Edad":1,
			"genero":"M",
			"Estado_esterilzacion":"Esterilizado",
			"Estado_salud":"test",
			"foto":file
		}
		print("FLAG")
		print(petdata)
		response = self.client.get("/agregar/")		
		response = self.client.post(reverse('users:agregar'),data=petdata,follow=True)
		form = response.context['form']
		print(form.errors)
		self.assertRedirects(response,"/agregar/")
		lm = [m for m in Mascota.objects.all()]
		response = self.client.get("/editar/{}".format(lm[0].id))
		print(response,Mascota.objects.count())











# Create your tests here.
