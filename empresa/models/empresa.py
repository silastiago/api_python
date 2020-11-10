from django.db import models
from crum import get_current_user
from django.contrib.auth.models import User
from core.models import  Pessoa

class Empresa(models.Model):

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome",
        help_text="Campo Obrigatório*",
        blank=True, null=True
    )

    cnpj = models.CharField(
        max_length=18,
        verbose_name="CNPJ",
        help_text="Campo Obrigatório*",
        blank=True, null=True
    )

    donos_empresas = models.ManyToManyField('Empresa', blank=True, related_name="Empresas")
    donos_pessoas = models.ManyToManyField(Pessoa, blank=True, null=True, related_name="Dono")

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name="Data de Atualização",
        auto_now=True
    )

    def __str__(self):
        return self.nome


    class Meta:
        app_label = "empresa"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"


