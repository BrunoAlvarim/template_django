from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class Funcionario(admin.ModelAdmin):
    #list_display = Define as colunas da tabela que serao exibidos na aba admin.
    list_display = ('id','nome','funcao','empresa')

    #list_display_links = define que eu clicando na coluna id ou coluna nome eu acesso o painel de edição
    list_display_links = ('id','nome')

    #list_filter = define as colunas que posso usar como filtro
    list_filter = ('empresa','funcao','flag_ativo')

    #define a paginação da tabela
    list_per_page = 10
    #Adiciona uma barra de busca no topo para fazer a busca
    search_fields = ('nome',)