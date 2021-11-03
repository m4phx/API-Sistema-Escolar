from rest_framework import serializers
from notas.models import Nota


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'
        # ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

