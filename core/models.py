from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.TextField(max_length=255)
    nacionalidade = models.CharField(max_length=100)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome