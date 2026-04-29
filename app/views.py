from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CadastroForm

# Create your views here.
@login_required
def home(request):
    return HttpResponse('test')

def cadastro(request):
    if request.method == 'GET':
        cadastro_form = CadastroForm
        return render(request, 'cinedu/cadastro.html', { 'cadastro_form': cadastro_form })
