from rest_framework import serializers
from prod_app import models as prod
from perf_app import models as perf

# === MODELOS DO prod_app ===
class UOSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.uo
        fields = '__all__'

class AtivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.ativo
        fields = '__all__'

class UEPSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.uep
        fields = '__all__'

class PocoSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.poco
        fields = '__all__'

class GrandezaIndustrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.grandeza_industrial
        fields = '__all__'

class GrandezaEspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.grandeza_especialista
        fields = '__all__'

class UnidadeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.unidade_medida
        fields = '__all__'

class UnidadeMedidaPadraoSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.unidade_medida_padrao
        fields = '__all__'

class VariavelIndustrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.variavel_industrial
        fields = '__all__'

class AnaliseSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.analise
        fields = '__all__'

class AmostraSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.amostra
        fields = '__all__'

class RelacaoEspecialistaIndustrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod.relacao_especialista_industrial
        fields = '__all__'

# === MODELOS DO perf_app ===
class UOPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.uo_perf
        fields = '__all__'

class AtivoPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.ativo_perf
        fields = '__all__'

class PocoPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.poco_perf
        fields = '__all__'

class GrandezaIndustrialPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.grandeza_industrial_perf
        fields = '__all__'

class GrandezaEspecialistaPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.grandeza_especialista_perf
        fields = '__all__'

class UnidadeMedidaPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.unidade_medida_perf
        fields = '__all__'

class UnidadeMedidaPadraoPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.unidade_medida_padrao_perf
        fields = '__all__'

class VariavelIndustrialPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.variavel_industrial_perf
        fields = '__all__'

class AnalisePerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.analise_perf
        fields = '__all__'

class AmostraPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.amostra_perf
        fields = '__all__'

class RelacaoEspecialistaIndustrialPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.relacao_especialista_industrial_perf
        fields = '__all__'

class ServidorPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.servidor_perf
        fields = '__all__'

class SondaPerfSerializer(serializers.ModelSerializer):
    class Meta:
        model = perf.sonda_perf
        fields = '__all__'
