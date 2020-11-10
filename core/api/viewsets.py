from rest_framework.viewsets import ModelViewSet
from core.models import Pessoa
from .serializers import PessoaSerializer
from empresa.models import Empresa
from rest_framework.decorators import action
from rest_framework.response import Response


class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer()
    filterset_fields = ['nome']

