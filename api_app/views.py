from rest_framework import viewsets
from prod_app import models as prod
from perf_app import models as perf
from . import serializers


from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# === ViewSets do prod_app ===

class UOViewSet(viewsets.ModelViewSet):
    queryset = prod.uo.objects.all()
    serializer_class = serializers.UOSerializer

class AtivoViewSet(viewsets.ModelViewSet):
    queryset = prod.ativo.objects.all()
    serializer_class = serializers.AtivoSerializer

    def get_queryset(self):
        queryset = prod.ativo.objects.all()
        uo_id = self.request.query_params.get('uo_id')
        if uo_id:
            queryset = queryset.filter(uo_id=uo_id)
        return queryset

class UEPViewSet(viewsets.ModelViewSet):
    queryset = prod.uep.objects.all()
    serializer_class = serializers.UEPSerializer

    def get_queryset(self):
        queryset = prod.uep.objects.all()
        ativo_id = self.request.query_params.get('ativo_id')
        if ativo_id:
            queryset = queryset.filter(ativo_id=ativo_id)
        return queryset

class PocoViewSet(viewsets.ModelViewSet):
    queryset = prod.poco.objects.all()
    serializer_class = serializers.PocoSerializer

    def get_queryset(self):
        queryset = prod.poco.objects.all()
        uep_id = self.request.query_params.get('uep_id')
        if uep_id:
            queryset = queryset.filter(uep_id=uep_id)
        return queryset

class GrandezaIndustrialViewSet(viewsets.ModelViewSet):
    queryset = prod.grandeza_industrial.objects.all()
    serializer_class = serializers.GrandezaIndustrialSerializer

class GrandezaEspecialistaViewSet(viewsets.ModelViewSet):
    queryset = prod.grandeza_especialista.objects.all()
    serializer_class = serializers.GrandezaEspecialistaSerializer

class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    queryset = prod.unidade_medida.objects.all()
    serializer_class = serializers.UnidadeMedidaSerializer

class UnidadeMedidaPadraoViewSet(viewsets.ModelViewSet):
    queryset = prod.unidade_medida_padrao.objects.all()
    serializer_class = serializers.UnidadeMedidaPadraoSerializer

class VariavelIndustrialViewSet(viewsets.ModelViewSet):
    queryset = prod.variavel_industrial.objects.all()
    serializer_class = serializers.VariavelIndustrialSerializer

class AnaliseViewSet(viewsets.ModelViewSet):
    queryset = prod.analise.objects.all()
    serializer_class = serializers.AnaliseSerializer

class AmostraViewSet(viewsets.ModelViewSet):
    queryset = prod.amostra.objects.all()
    serializer_class = serializers.AmostraSerializer

class RelacaoEspecialistaIndustrialViewSet(viewsets.ModelViewSet):
    queryset = prod.relacao_especialista_industrial.objects.all()
    serializer_class = serializers.RelacaoEspecialistaIndustrialSerializer

# === ViewSets do perf_app ===

class UOPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.uo_perf.objects.all()
    serializer_class = serializers.UOPerfSerializer

class AtivoPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.ativo_perf.objects.all()
    serializer_class = serializers.AtivoPerfSerializer

class PocoPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.poco_perf.objects.all()
    serializer_class = serializers.PocoPerfSerializer

class GrandezaIndustrialPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.grandeza_industrial_perf.objects.all()
    serializer_class = serializers.GrandezaIndustrialPerfSerializer

class GrandezaEspecialistaPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.grandeza_especialista_perf.objects.all()
    serializer_class = serializers.GrandezaEspecialistaPerfSerializer

class UnidadeMedidaPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.unidade_medida_perf.objects.all()
    serializer_class = serializers.UnidadeMedidaPerfSerializer

class UnidadeMedidaPadraoPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.unidade_medida_padrao_perf.objects.all()
    serializer_class = serializers.UnidadeMedidaPadraoPerfSerializer

class VariavelIndustrialPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.variavel_industrial_perf.objects.all()
    serializer_class = serializers.VariavelIndustrialPerfSerializer

class AnalisePerfViewSet(viewsets.ModelViewSet):
    queryset = perf.analise_perf.objects.all()
    serializer_class = serializers.AnalisePerfSerializer

class AmostraPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.amostra_perf.objects.all()
    serializer_class = serializers.AmostraPerfSerializer

class RelacaoEspecialistaIndustrialPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.relacao_especialista_industrial_perf.objects.all()
    serializer_class = serializers.RelacaoEspecialistaIndustrialPerfSerializer

class ServidorPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.servidor_perf.objects.all()
    serializer_class = serializers.ServidorPerfSerializer

class SondaPerfViewSet(viewsets.ModelViewSet):
    queryset = perf.sonda_perf.objects.all()
    serializer_class = serializers.SondaPerfSerializer
