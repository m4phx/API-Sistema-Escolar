from rest_framework import viewsets
from notas.models import Nota
from notas.serializer import NotaSerializer


class NotaViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
