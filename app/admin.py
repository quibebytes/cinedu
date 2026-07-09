from django.contrib import admin
from .models import Documentario, Favorito, Usuario, RegistroSessao

admin.site.register(Usuario)
admin.site.register(RegistroSessao)
admin.site.register(Documentario)
admin.site.register(Favorito)
