from django import forms
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Nome',
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'placeholder': 'Digite o seu nome',
            'id': 'nome',
            'name': 'username',
            'autocomplete': 'username',
            'required': True,
        }),
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'id': 'senha',
            'name': 'password',
            'placeholder': 'Digite a sua senha',
            'autocomplete': 'current-password',
            'required': True,
        }),
    )


class CadastroForm(UserCreationForm):
    palavra_chave = forms.CharField(
        label='Palavra-chave',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite uma palavra importante para você',
            'id': 'chave',
            'name': 'chave',
            'required': False,
        }),
    )

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ['username', 'password1', 'password2']


class AlterarSenhaForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ['password1', 'password2']
