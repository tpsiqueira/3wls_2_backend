# api_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views_custom

router = DefaultRouter()

# ViewSets do prod_app
router.register(r'uos', UOViewSet)
router.register(r'ativos', AtivoViewSet)
router.register(r'ueps', UEPViewSet)
router.register(r'pocos', PocoViewSet)
router.register(r'grandezas-industriais', GrandezaIndustrialViewSet)
router.register(r'grandezas-especialistas', GrandezaEspecialistaViewSet)
router.register(r'unidades-medida', UnidadeMedidaViewSet)
router.register(r'unidades-medida-padrao', UnidadeMedidaPadraoViewSet)
router.register(r'variaveis-industriais', VariavelIndustrialViewSet)
router.register(r'analises', AnaliseViewSet)
router.register(r'amostras', AmostraViewSet)
router.register(r'relacoes-especialistas-industriais', RelacaoEspecialistaIndustrialViewSet)

# ViewSets do perf_app
router.register(r'uos-perf', UOPerfViewSet)
router.register(r'ativos-perf', AtivoPerfViewSet)
router.register(r'pocos-perf', PocoPerfViewSet)
router.register(r'grandezas-industriais-perf', GrandezaIndustrialPerfViewSet)
router.register(r'grandezas-especialistas-perf', GrandezaEspecialistaPerfViewSet)
router.register(r'unidades-medida-perf', UnidadeMedidaPerfViewSet)
router.register(r'unidades-medida-padrao-perf', UnidadeMedidaPadraoPerfViewSet)
router.register(r'variaveis-industriais-perf', VariavelIndustrialPerfViewSet)
router.register(r'analises-perf', AnalisePerfViewSet)
router.register(r'amostras-perf', AmostraPerfViewSet)
router.register(r'relacoes-especialistas-industriais-perf', RelacaoEspecialistaIndustrialPerfViewSet)
router.register(r'servidores-perf', ServidorPerfViewSet)
router.register(r'sondas-perf', SondaPerfViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Endpoints customizados (REST)
    path('selecionar-ge-amostra/', views_custom.SelecionarGeAmostraAPIView.as_view()),
    path('carregar-instancias/', views_custom.CarregarInstanciasAPIView.as_view()),
    path('carregar-instancia-por-ge/', views_custom.CarregarInstanciasPorGeAPIView.as_view()),
    path('carregar-amostras/', views_custom.CarregarAmostrasAPIView.as_view()),
    path('instancia/adicionar/', views_custom.AdicionarInstanciaAPIView.as_view()),
    path('instancia/editar/', views_custom.EditarInstanciaAPIView.as_view()),
    path('instancia/excluir/', views_custom.ExcluirInstanciaAPIView.as_view()),
    path('instancia/ativar/', views_custom.AtivarInstanciaAPIView.as_view()),
    path('instancia/desativar/', views_custom.DesativarInstanciaAPIView.as_view()),
]

# api_app/views.py
from rest_framework import viewsets
from prod_app import models as prod
from perf_app import models as perf
from . import serializers

# === ViewSets do prod_app ===
class UOViewSet(viewsets.ModelViewSet): queryset = prod.uo.objects.all(); serializer_class = serializers.UOSerializer
class AtivoViewSet(viewsets.ModelViewSet): queryset = prod.ativo.objects.all(); serializer_class = serializers.AtivoSerializer
class UEPViewSet(viewsets.ModelViewSet): queryset = prod.uep.objects.all(); serializer_class = serializers.UEPSerializer
class PocoViewSet(viewsets.ModelViewSet): queryset = prod.poco.objects.all(); serializer_class = serializers.PocoSerializer
class GrandezaIndustrialViewSet(viewsets.ModelViewSet): queryset = prod.grandeza_industrial.objects.all(); serializer_class = serializers.GrandezaIndustrialSerializer
class GrandezaEspecialistaViewSet(viewsets.ModelViewSet): queryset = prod.grandeza_especialista.objects.all(); serializer_class = serializers.GrandezaEspecialistaSerializer
class UnidadeMedidaViewSet(viewsets.ModelViewSet): queryset = prod.unidade_medida.objects.all(); serializer_class = serializers.UnidadeMedidaSerializer
class UnidadeMedidaPadraoViewSet(viewsets.ModelViewSet): queryset = prod.unidade_medida_padrao.objects.all(); serializer_class = serializers.UnidadeMedidaPadraoSerializer
class VariavelIndustrialViewSet(viewsets.ModelViewSet): queryset = prod.variavel_industrial.objects.all(); serializer_class = serializers.VariavelIndustrialSerializer
class AnaliseViewSet(viewsets.ModelViewSet): queryset = prod.analise.objects.all(); serializer_class = serializers.AnaliseSerializer
class AmostraViewSet(viewsets.ModelViewSet): queryset = prod.amostra.objects.all(); serializer_class = serializers.AmostraSerializer
class RelacaoEspecialistaIndustrialViewSet(viewsets.ModelViewSet): queryset = prod.relacao_especialista_industrial.objects.all(); serializer_class = serializers.RelacaoEspecialistaIndustrialSerializer

# === ViewSets do perf_app ===
class UOPerfViewSet(viewsets.ModelViewSet): queryset = perf.uo_perf.objects.all(); serializer_class = serializers.UOPerfSerializer
class AtivoPerfViewSet(viewsets.ModelViewSet): queryset = perf.ativo_perf.objects.all(); serializer_class = serializers.AtivoPerfSerializer
class PocoPerfViewSet(viewsets.ModelViewSet): queryset = perf.poco_perf.objects.all(); serializer_class = serializers.PocoPerfSerializer
class GrandezaIndustrialPerfViewSet(viewsets.ModelViewSet): queryset = perf.grandeza_industrial_perf.objects.all(); serializer_class = serializers.GrandezaIndustrialPerfSerializer
class GrandezaEspecialistaPerfViewSet(viewsets.ModelViewSet): queryset = perf.grandeza_especialista_perf.objects.all(); serializer_class = serializers.GrandezaEspecialistaPerfSerializer
class UnidadeMedidaPerfViewSet(viewsets.ModelViewSet): queryset = perf.unidade_medida_perf.objects.all(); serializer_class = serializers.UnidadeMedidaPerfSerializer
class UnidadeMedidaPadraoPerfViewSet(viewsets.ModelViewSet): queryset = perf.unidade_medida_padrao_perf.objects.all(); serializer_class = serializers.UnidadeMedidaPadraoPerfSerializer
class VariavelIndustrialPerfViewSet(viewsets.ModelViewSet): queryset = perf.variavel_industrial_perf.objects.all(); serializer_class = serializers.VariavelIndustrialPerfSerializer
class AnalisePerfViewSet(viewsets.ModelViewSet): queryset = perf.analise_perf.objects.all(); serializer_class = serializers.AnalisePerfSerializer
class AmostraPerfViewSet(viewsets.ModelViewSet): queryset = perf.amostra_perf.objects.all(); serializer_class = serializers.AmostraPerfSerializer
class RelacaoEspecialistaIndustrialPerfViewSet(viewsets.ModelViewSet): queryset = perf.relacao_especialista_industrial_perf.objects.all(); serializer_class = serializers.RelacaoEspecialistaIndustrialPerfSerializer
class ServidorPerfViewSet(viewsets.ModelViewSet): queryset = perf.servidor_perf.objects.all(); serializer_class = serializers.ServidorPerfSerializer
class SondaPerfViewSet(viewsets.ModelViewSet): queryset = perf.sonda_perf.objects.all(); serializer_class = serializers.SondaPerfSerializer
