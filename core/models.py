from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_cadastro = models.CharField(max_length=20, choices=[('atleta', 'Atleta'), ('treinador', 'Treinador'), ('outros', 'Outros')])

    def __str__(self):
        return self.user.username  