import django.contrib.messages as messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout as auth_logout
from .forms import CadastroForm
from .models import Favorito, Documentario

# Create your views here.
@login_required
def home(request):
    return render(request, 'cinedu/home.html', { 'usuario': request.user })

@login_required
def favoritos(request):
    favoritos = Documentario.objects.filter(favorito__usuario_id=request.user.id)
    return render(request, 'cinedu/favoritos.html', { 'favoritos': favoritos, 'usuario': request.user })

@login_required
def detalhes(request, doc_id):
    documentario = get_object_or_404(Documentario, id=doc_id)
    return render(request, 'cinedu/detalhes.html', { 'documentario': documentario, 'usuario': request.user })

@login_required
def pesquisa(request):
    return render(request, 'cinedu/pesquisa.html', { 'usuario': request.user })

@login_required
def video(request, doc_id):
    documentario = get_object_or_404(Documentario, id=doc_id)
    return render(request, 'cinedu/video.html', { 'documentario': documentario })

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponse("Log out realizado com sucesso.")



def cadastro(request):
    if request.method == 'GET':
        cadastro_form = CadastroForm()
        return render(request, 'cinedu/cadastro.html', { 'cadastro_form': cadastro_form, 'style_path': 'style.css' })

    if request.method == 'POST':
        cadastro_form = CadastroForm(request.POST)
        if cadastro_form.is_valid():
            usuario = cadastro_form.save(commit=False)
            usuario.username = usuario.username.lower()
            usuario.palavra_chave = cadastro_form.cleaned_data['palavra_chave'].lower().strip()
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso.')
            login(request, usuario)
            return redirect('cinedu:home')
        else:
            return render(request, 'cinedu/cadastro.html', { 'cadastro_form': cadastro_form, 'style_path': 'style.css' })
