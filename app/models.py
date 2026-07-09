from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser, models.Model):
    palavra_chave = models.CharField(max_length=50, blank=True, verbose_name='palavra-chave')

    class Meta:
        verbose_name = 'Usuário'


class Documentario(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    sinopse = models.TextField()
    data_publicacao = models.DateField()
    duracao = models.DurationField()
    thumbnail = models.ImageField(upload_to='thumbnails/',blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Documentário'

class RegistroSessao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    documentario = models.ForeignKey(Documentario, on_delete=models.CASCADE)
    ultimo_segundo = models.DurationField()

    def __str__(self):
        return f'{self.usuario.username} assistiu "{self.documentario.titulo}" até {self.ultimo_segundo}'

    class Meta:
        unique_together = ('usuario', 'documentario')
        verbose_name = 'Registro da Sessão'
        verbose_name_plural = 'Registros das Sessões'


class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    documentario = models.ForeignKey(Documentario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} ❤️ "{self.documentario.titulo}"'

    class Meta:
        unique_together = ('usuario', 'documentario')
