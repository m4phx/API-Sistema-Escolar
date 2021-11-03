from django.db import models
from alunos.models import Aluno

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    valor = models.IntegerField()

    def __str__(self):
        return str(self.valor)
