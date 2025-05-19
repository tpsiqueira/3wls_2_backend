from django.contrib import admin
from .models import (
    uo_perf,
    ativo_perf,
    poco_perf,
    unidade_medida_padrao_perf,
    unidade_medida_perf,
    grandeza_industrial_perf,
    grandeza_especialista_perf,
    variavel_industrial_perf,
    relacao_especialista_industrial_perf,
    sonda_perf,
    servidor_perf,
    lookup_servidor_perf,
    analise_perf,
    amostra_perf,
)

admin.site.register(uo_perf)
admin.site.register(ativo_perf)
admin.site.register(poco_perf)
admin.site.register(unidade_medida_padrao_perf)
admin.site.register(unidade_medida_perf)
admin.site.register(grandeza_industrial_perf)
admin.site.register(grandeza_especialista_perf)
admin.site.register(variavel_industrial_perf)
admin.site.register(relacao_especialista_industrial_perf)
admin.site.register(sonda_perf)
admin.site.register(servidor_perf)
admin.site.register(lookup_servidor_perf)
admin.site.register(analise_perf)
admin.site.register(amostra_perf)
