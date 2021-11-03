from django.db import models
from cursos.models import Curso


class Materia(models.Model):
    nome = models.CharField(max_length=30)
    carga_horaria = models.CharField(max_length=3)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome