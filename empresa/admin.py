from django.contrib import admin
from .models.empresa import Empresa

# Register your models here.

class EmpresaInline(admin.StackedInline):
	model = Empresa
	fields = [
		'nome',
		'cnpj',
	]
	extra = 0



@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
	autocomplete_fields = ['donos_empresas', 'donos_pessoas']
	search_fields = ['donos_empresas', 'donos_pessoas']

	fieldsets = (
		('Dados Principais', {'fields': (
			'nome',
			'cnpj',
			'donos_empresas',
			'donos_pessoas'
		)}),
	)


