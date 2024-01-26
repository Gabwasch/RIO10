from django.contrib import admin
from .models import Perfil
# Register your models here.
# Registrei para que o admin possa cadastrar usuários do modelo Pessoa
admin.site.register(Perfil)