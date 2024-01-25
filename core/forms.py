# core/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Pessoa

class CadastroForm(UserCreationForm):
    # Se necessário, adicione campos personalizados aqui
    class Meta:
        model = Pessoa
        fields = ['nome', 'username', 'email', 'data_nascimento', 'nacionalidade', 'senha']
        
class CustomAuthenticationForm(AuthenticationForm):
    # Se necessário, adicione campos personalizados aqui
    class Meta:
        model = Pessoa
        fields = ['username', 'senha']