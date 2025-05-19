from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from prod_app.models import (
    poco, grandeza_especialista, grandeza_industrial,
    relacao_especialista_industrial, variavel_industrial,
    unidade_medida, analise, amostra
)
from django.contrib.auth.models import User

from django.core.serializers import serialize

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def selecionar_ge_amostra_especialista(request):
    try:
        poco_sel = poco.objects.get(id=int(request.data.get("poco")))
        ge_sel = grandeza_especialista.objects.get(id=int(request.data.get("grandeza_especialista")))

        grandezas_industriais_rel = relacao_especialista_industrial.objects.filter(
            especialista=ge_sel
        )

        variaveis_industriais_sel = []
        for item in grandezas_industriais_rel:
            vi = variavel_industrial.objects.filter(poco=poco_sel, grandeza_industrial=item.industrial).first()
            if vi:
                variaveis_industriais_sel.append(vi)

        return Response({
            "variaveis_industriais": serialize("json", variaveis_industriais_sel),
            "saida": True
        })
    except Exception as e:
        return Response({
            "variaveis_industriais": "",
            "saida": False,
            "erro": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def carregar_instancias_por_ge(request):
    try:
        ge_id = int(request.data.get("grandeza_especialista"))
        lista_analises = analise.objects.filter(grandeza_especialista=ge_id)
        return Response({
            "analises": serialize("json", lista_analises),
            "saida": True
        })
    except Exception as e:
        return Response({
            "analises": "",
            "saida": False,
            "erro": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def carregar_amostras_por_analise(request):
    try:
        analise_id = int(request.data.get("analise"))
        lista_amostras = amostra.objects.filter(analise=analise_id).order_by("inicio")
        return Response({
            "amostras": serialize("json", lista_amostras),
            "saida": True
        })
    except Exception as e:
        return Response({
            "amostras": "",
            "saida": False,
            "erro": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def carregar_instancias(request):
    try:
        lista_analises = analise.objects.all()
        return Response({
            "analises": serialize("json", lista_analises),
            "saida": True
        })
    except Exception as e:
        return Response({
            "analises": "",
            "saida": False,
            "erro": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def excluir_instancia(request):
    try:
        pk = request.data.get("pk")
        analise_sel = analise.objects.get(id=int(pk))
        analise_sel.delete()
        return Response({"saida": True})
    except Exception as e:
        return Response({"saida": False, "erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ativar_instancia(request):
    try:
        if request.user.groups.filter(name="validador").exists():
            pk = request.data.get("pk")
            analise_sel = analise.objects.get(id=int(pk))
            analise_sel.exportacao_habilitada = True
            analise_sel.save()
            return Response({"saida": True})
        return Response({"saida": False}, status=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        return Response({"saida": False, "erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def desativar_instancia(request):
    try:
        if request.user.groups.filter(name="validador").exists():
            pk = request.data.get("pk")
            analise_sel = analise.objects.get(id=int(pk))
            analise_sel.exportacao_habilitada = False
            analise_sel.save()
            return Response({"saida": True})
        return Response({"saida": False}, status=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        return Response({"saida": False, "erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)
