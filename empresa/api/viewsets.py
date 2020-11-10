from rest_framework.viewsets import ModelViewSet
from empresa.models import Empresa
from .serializers import EmpresaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    filterset_fields = ['nome']


    @action(detail=True, methods=['get'])
    def donos(self, request, pk=None):

        empresas = Empresa.objects.filter(
            donos_empresas__in=[pk]
        )

        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def pessoas(self, request, pk=None):
        empresas = Empresa.objects.filter(
            donos_pessoas__in=[pk]
        )

        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)