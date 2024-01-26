from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=100)
    senha = models.CharField(max_length=255)

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_cadastro = models.CharField(max_length=20, choices=[('atleta', 'Atleta'), ('treinador', 'Treinador'), ('outros', 'Outros')])

    def __str__(self):
        return self.user.username  