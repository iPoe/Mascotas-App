from django.contrib import admin
from users.models import usuarios, Fundacion, Mascota, Match, Contenido_Multi

admin.site.register(usuarios)
admin.site.register(Fundacion)
admin.site.register(Mascota)
admin.site.register(Match)
admin.site.register(Contenido_Multi)
# Register your models here.

