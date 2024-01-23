# core/views.py
from django.shortcuts import render, redirect
from .forms import CadastroForm

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # Isso salva os dados no banco de dados
            except Exception as e:
                print(f"Erro ao salvar no banco de dados: {e}")
            return redirect('cadastro')  # Pode redirecionar para outra página após o cadastro
    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form})
