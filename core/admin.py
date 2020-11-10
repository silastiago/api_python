from django.contrib import admin
from .models.pessoa import Pessoa


# Register your models here.


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
	search_fields = ['nome']

	fieldsets = (
		('Dados Principais', {'fields': (
			'nome',
			'cpf',
            'rg'
		)}),
	)
