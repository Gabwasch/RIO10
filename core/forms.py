from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Pessoa

class CadastroForm(UserCreationForm):
    # Adicione campos personalizados aqui
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    tipo_cadastro = forms.ChoiceField(choices=[('atleta', 'Atleta'), ('treinador', 'Treinador'), ('outros', 'Outros')])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        perfil = Perfil.objects.create(user=user, tipo_cadastro=self.cleaned_data['tipo_cadastro'])

        return user

class CustomAuthenticationForm(AuthenticationForm):
    # Se necessário, adicione campos personalizados aqui
    class Meta:
        model = Pessoa
        fields = ['username', 'senha']
