from django.urls import path
from . import views_perf


urlpatterns = [
          
    path("rotulagem_perf", views_perf.rotulagem_perf, name="Rotulagem Perf"),
    path("rotulagem_perf/<uo>", views_perf.rotulagem_perf, name="Rotulagem Perf"),
    path("rotulagem_perf/<uo>/<ativo>", views_perf.rotulagem_perf, name="Rotulagem Perf"),
    path("rotulagem_perf/<uo>/<ativo>/<poco>", views_perf.rotulagem_perf, name="Rotulagem Perf"),    
    path("rotulagem_perf/<uo>/<ativo>/<poco>/<inicio>", views_perf.rotulagem_perf, name="Rotulagem Perf"),    
    path("rotulagem_perf/<uo>/<ativo>/<poco>/<inicio>/<fim>", views_perf.rotulagem_perf, name="Rotulagem Perf"),    
    
    path("ajax/perf/pocos", views_perf.pocos_perf),    
    path("ajax/perf/selecionar_ge_amostra_especialista", views_perf.ajax_selecionar_ge_amostra_especialista_perf),    
    path("ajax/perf/obter_dados_variaveis_entrada", views_perf.ajax_coletar_dados_variaveis_entrada_perf),
    path("ajax/perf/adicionar_instancia_amostras_especialista", views_perf.ajax_adicionar_instancia_amostras_especialista_perf),
    path("ajax/perf/editar_instancia_amostras_especialista", views_perf.ajax_editar_instancia_amostras_especialista_perf),    
    path("ajax/perf/carregar_instancias_por_ge", views_perf.ajax_carregar_instancia_por_ge_perf),
    path("ajax/perf/carregar_instancias", views_perf.ajax_carregar_instancias_perf),
    path("ajax/perf/carregar_amostras_por_analise", views_perf.ajax_carregar_amostras_por_instancia_perf),
    path("ajax/perf/excluir_instancia_por_id", views_perf.ajax_excluir_instancia_por_id_perf)    
]
