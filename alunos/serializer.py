from rest_framework import serializers
from alunos.models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        # ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

