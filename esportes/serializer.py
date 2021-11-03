from rest_framework import serializers
from esportes.models import Esporte


class EsporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esporte
        fields = '__all__'
        # ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

