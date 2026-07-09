from django.contrib import admin
from .models import Documentario, Favorito, Usuario, RegistroSessao, Categoria

admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(RegistroSessao)
admin.site.register(Documentario)
admin.site.register(Favorito)
