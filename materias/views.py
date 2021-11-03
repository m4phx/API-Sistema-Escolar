from rest_framework import viewsets
from materias.models import Materia
from materias.serializer import MateriaSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os alunos e alunas"""
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
