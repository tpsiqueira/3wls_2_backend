from django.urls import path
from . import views
from . import views_prod

urlpatterns = [
    path('home/', views.home, name='Home'),
    path("", views_prod.index, name="index"),
    path("rotulagem/", views_prod.rotulagem, name="Rotulagem"),
    path("exportacao/", views_prod.exportacao, name="Exportação"),
    path("rotulagem_perf/", views_prod.rotulagem, name="RotulagemPerf"), 

    path("ajax/selecionar_ge_amostra_especialista", views_prod.ajax_selecionar_ge_amostra_especialista),
    path("ajax/obter_dados_variaveis_entrada", views_prod.ajax_coletar_dados_variaveis_entrada),
    path("ajax/adicionar_instancia_amostras_especialista", views_prod.ajax_adicionar_instancia_amostras_especialista),
    path("ajax/editar_instancia_amostras_especialista", views_prod.ajax_editar_instancia_amostras_especialista),
    path("ajax/carregar_instancias_por_ge", views_prod.ajax_carregar_instancia_por_ge),
    path("ajax/carregar_instancias", views_prod.ajax_carregar_instancias),
    path("ajax/carregar_amostras_por_analise", views_prod.ajax_carregar_amostras_por_instancia),
    path("ajax/excluir_instancia_por_id", views_prod.ajax_excluir_instancia_por_id),
    path("ajax/ativar_instancia", views_prod.ajax_ativar_instancia),
    path("ajax/desativar_intancia", views_prod.ajax_desativar_instancia),

    path("ajax_adicionar_unidade_operacional", views.ajax_adicionar_uo),
    path("ajax_editar_unidade_operacional", views.ajax_editar_uo),
    path("ajax_excluir_unidade_operacional", views.ajax_excluir_uo),
    path("ajax_adicionar_ativo", views.ajax_adicionar_ativo),
    path("ajax_editar_ativo", views.ajax_editar_ativo),
    path("ajax_excluir_ativo", views.ajax_excluir_ativo),
    path("ajax_adicionar_uep", views.ajax_adicionar_uep),
    path("ajax_editar_uep", views.ajax_editar_uep),
    path("ajax_excluir_uep", views.ajax_excluir_uep),
    path("ajax_adicionar_poco", views.ajax_adicionar_poco),
    path("ajax_editar_poco", views.ajax_editar_poco),
    path("ajax_excluir_poco", views.ajax_excluir_poco),
    path("ajax_adicionar_variavel_industrial", views.ajax_adicionar_variavel_industrial),
    path("ajax_editar_variavel_industrial", views.ajax_editar_variavel_industrial),
    path("ajax_excluir_variavel_industrial", views.ajax_excluir_variavel_industrial),

   
]
