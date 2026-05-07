import django.contrib.messages as messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import CadastroForm

# Create your views here.
@login_required
def home(request):
    return HttpResponse('test')

def cadastro(request):
    if request.method == 'GET':
        cadastro_form = CadastroForm()
        return render(request, 'cinedu/cadastro.html', { 'cadastro_form': cadastro_form })

    if request.method == 'POST':
        cadastro_form = CadastroForm(request.POST)
        if cadastro_form.is_valid():
            usuario = cadastro_form.save(commit=False)
            usuario.username = usuario.username.lower()
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso.')
            login(request, usuario)
            return redirect('cinedu:home')
        else:
            return render(request, 'cinedu/cadastro.html', {'cadastro_form': cadastro_form})
