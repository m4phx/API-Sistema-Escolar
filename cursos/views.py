from rest_framework import viewsets
from cursos.models import Curso
from cursos.serializer import CursoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer



