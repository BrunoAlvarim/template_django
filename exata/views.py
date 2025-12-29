from rest_framework import viewsets
from .serializers import FuncionarioSerializers
from .models import Funcionario

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializers
