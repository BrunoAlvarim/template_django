from rest_framework import serializers
from .models import Funcionario

class FuncionarioSerializers(serializers.ModelSerializer):
    class Meta(): # class meta serve para configurarmos a class principal
        model = Funcionario #indica qual model meu serializer vai ler
        fields = ['id','nome','funcao','empresa','flag_ativo'] #indica quais colunas meu serializer vai ler do meu model