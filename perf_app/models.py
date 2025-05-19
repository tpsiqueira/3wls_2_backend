#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
import datetime


class uo_perf(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome


class ativo_perf(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    uo = models.ForeignKey(uo_perf, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class poco_perf(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    ativo = models.ForeignKey(
        ativo_perf, null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome


class unidade_medida_padrao_perf(models.Model): ##verificar chamada para perf
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome


class unidade_medida_perf(models.Model): ##verificar chamada para perf
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    unidade_medida_padrao = models.ForeignKey(
        unidade_medida_padrao_perf, on_delete=models.SET_NULL, null=True, blank=True
    )
    coeficiente_angular = models.FloatField(null=True, blank=True)
    coeficiente_linear = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nome


class grandeza_industrial_perf(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    um = models.CharField(max_length=50, null=True, blank=True)
    localizacao = models.CharField(max_length=50, null=True, blank=True)
    origem = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.nome


class grandeza_especialista_perf(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)
    rotulo_normalidade = models.IntegerField(default=0, null=True, blank=True)
    rotulo_transient = models.IntegerField(default=0, null=True, blank=True)
    rotulo_steady_state = models.IntegerField(default=0, null=True, blank=True)
    periodo_amostra_inicial_nao_rotulada = models.IntegerField(
        default=0, null=True, blank=True
    )

    def __str__(self):
        return self.nome


class variavel_industrial_perf(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=True, blank=True)
    poco = models.ForeignKey(poco_perf, null=True, blank=True, on_delete=models.CASCADE)
    grandeza_industrial = models.ForeignKey(
        grandeza_industrial_perf, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("grandeza_industrial", "poco")

    def __str__(self):
        return self.nome


class relacao_especialista_industrial_perf(models.Model):
    especialista = models.ForeignKey(
        grandeza_especialista_perf, null=True, blank=True, on_delete=models.CASCADE
    )
    industrial = models.ForeignKey(
        grandeza_industrial_perf, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("especialista", "industrial")

    def __str__(self):
        return str(self.especialista.nome + "/" + self.industrial.nome)


## Migraçao de funções do models monitor_app


class sonda_perf(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome


class servidor_perf(models.Model):
    nome = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome


class lookup_servidor_perf(models.Model):
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    sonda = models.ForeignKey(sonda_perf, on_delete=models.CASCADE)
    servidor = models.ForeignKey(servidor_perf, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("sonda", "servidor")

    def __str__(self):
        return str(self.sonda.nome + "/" + self.servidor.nome)


class analise_perf(models.Model):
    grandeza_especialista = models.ForeignKey(
        grandeza_especialista_perf, on_delete=models.CASCADE
    )
    poco = models.ForeignKey(poco_perf, on_delete=models.CASCADE)
    sonda = models.ForeignKey(sonda_perf, on_delete=models.CASCADE)
    servidor = models.ForeignKey(servidor_perf, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(default=timezone.now)
    data_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField(default=timezone.now)
    exportacao_habilitada = models.BooleanField()
    ChoiceList = (
        ("Pendente", "Pendente"),
        ("Exportando", "Exportando"),
        ("Exportada", "Exportada"),
        ("Erro", "Erro"),
    )
    status_exportacao = models.CharField(
        default="Pendente",
        max_length=15,
        choices=ChoiceList,
        null=True,
        blank=True,
    )

    def __int__(self):
        return self.id


class amostra_perf(models.Model):
    analise = models.ForeignKey(analise_perf, on_delete=models.CASCADE)
    inicio = models.DateTimeField(default=timezone.now)
    fim = models.DateTimeField(default=timezone.now)
    choice_list = (
        ("NORMAL", "NORMAL"),
        ("TRANSIENT", "TRANSIENT"),
        ("STEADY STATE", "STEADY STATE"),
        ("UNKNOWN", "UNKNOWN"),
    )
    tipo = models.CharField(default="NORMAL", max_length=30, choices=choice_list)
