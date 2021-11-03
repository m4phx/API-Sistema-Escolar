from rest_framework import viewsets
from alunos.models import Aluno
from alunos.serializer import AlunoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


