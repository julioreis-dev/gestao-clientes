from django.contrib import admin
from produtos.models.produtos import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'preco')


admin.site.register(Produto, ProdutoAdmin)
