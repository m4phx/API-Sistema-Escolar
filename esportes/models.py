from django.db import models


class Esporte(models.Model):
    TIPO = (
        ('B', 'Bola'),
        ('P', 'Peso'),
        ('A', 'Aquático')
    )
    nome = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False, default='P')

    def __str__(self):
        return self.descricao