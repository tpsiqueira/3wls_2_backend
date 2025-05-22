from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'usuarios', UserViewSet)

# === Rotas do prod_app ===
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

# === Rotas do perf_app ===
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
]
