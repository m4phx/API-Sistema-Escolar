from rest_framework import serializers
from materias.models import Materia


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'
        # ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

