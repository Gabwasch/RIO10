from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=100)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
