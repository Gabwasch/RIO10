from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomAuthenticationForm, CadastroForm
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('index')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('minha_area')
        else:
            messages.error(request, 'Erro ao fazer login. Verifique suas credenciais.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def minha_area(request):
    return render(request, 'minha_area.html')