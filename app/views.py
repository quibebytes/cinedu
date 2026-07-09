import random
import django.contrib.messages as messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout as auth_logout
from django.db.models import Q
from .forms import CadastroForm, AlterarSenhaForm
from .models import Favorito, Documentario, Usuario, Categoria


@login_required
def home(request):

    # fazer query de um documentario aleatorio
    pks = Documentario.objects.values_list('pk', flat=True)
    pk_aleatoria = random.choice(pks)
    documentario_feature = Documentario.objects.get(pk=pk_aleatoria)

    categorias = Categoria.objects.all()[:50]

    documentarios_dicio = {}

    for cat in categorias:
        documentarios_dicio[cat.nome] = Documentario.objects.filter(categoria__id=cat.id)

    return render(request, 'cinedu/home.html', {
        'usuario': request.user,
        'documentario_feature': documentario_feature,
        'documentarios_dicio': documentarios_dicio,
    })

@login_required
def favoritos(request):
    favoritos = Documentario.objects.filter(favorito__usuario_id=request.user.id)
    return render(request, 'cinedu/favoritos.html', { 'favoritos': favoritos, 'usuario': request.user })

@login_required
def detalhes(request, doc_id):
    documentario = get_object_or_404(Documentario, id=doc_id)
    favoritado = Favorito.objects.filter(Q(usuario_id=request.user.id) & Q(documentario_id=doc_id)).exists()

    if request.method == 'POST' and request.POST['botao_clicado'] == 'fav':
        if favoritado:
           fav_obj = Favorito.objects.get(Q(usuario_id=request.user.id) & Q(documentario_id=doc_id)) 
           fav_obj.delete()
        else:
            fav_obj = Favorito(usuario=request.user, documentario=documentario)
            fav_obj.save()

        favoritado = not favoritado

    return render(request, 'cinedu/detalhes.html', {
        'documentario': documentario,
        'usuario': request.user,
        'favoritado': favoritado,
    })

@login_required
def pesquisa(request, cat_id=None):
    categorias = Categoria.objects.all()
    if cat_id:
        documentarios = Documentario.objects.filter(categoria__id=cat_id)
    else:
        documentarios = Documentario.objects.all()

    termos = None

    # Pesquisa simples de substrings
    if request.method == 'POST':
        termos = request.POST.get('termos_de_pesquisa').strip();
        documentarios = documentarios.filter(
            Q(titulo__contains=termos)          |
            Q(autor__contains=termos)           |
            Q(data_publicacao__contains=termos) |
            Q(sinopse__contains=termos)         
        )

    return render(request, 'cinedu/pesquisa.html', {
        'usuario': request.user,
        'categorias': categorias,
        'categoria_atual': Categoria.objects.get(id=cat_id).nome if cat_id else None,
        'documentarios': documentarios,
        'termos': termos,
    })

@login_required
def video(request, doc_id):
    documentario = get_object_or_404(Documentario, id=doc_id)
    return render(request, 'cinedu/video.html', { 'documentario': documentario })

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponse('Logout realizado com sucesso.')

def cadastro(request):
    if request.method == 'GET':
        cadastro_form = CadastroForm()
        return render(request, 'cinedu/cadastro.html', { 'cadastro_form': cadastro_form })

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
            return render(request, 'cinedu/cadastro.html', { 'cadastro_form': cadastro_form })

@login_required
def alterar_senha(request):
    if request.method == 'GET':
        senha_form = AlterarSenhaForm()
        return render(request, 'cinedu/alterar_senha.html', { 'senha_form': senha_form })

    if request.method == 'POST':
        senha_form = AlterarSenhaForm(request.POST)
        if senha_form.is_valid():
            request.user.set_password(senha_form.cleaned_data.get('password1'))
            request.user.save()
            messages.success(request, 'Alteração de senha realizada com sucesso.')
            return redirect('cinedu:home')
        else:
            return render(request, 'cinedu/alterar_senha.html', { 'senha_form': senha_form })
