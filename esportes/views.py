from rest_framework import viewsets
from esportes.models import Esporte
from esportes.serializer import EsporteSerializer


class EsporteViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Esporte.objects.all()
    serializer_class = EsporteSerializer
