from django.db import models

class Documentario(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    sinopse = models.CharField(max_length=2500)
    data_publicacao = models.DateField()
    duracao = models.DurationField()
    ultimo_segundo = models.DurationField()
    thumbnail = models.ImageField(upload_to='thumbnails/',blank=True, null=True)

    def __str__(self):
        return self.titulo
