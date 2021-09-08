from django.contrib import admin
from vendas.actions.vendas import nfe_true, nfe_false
from vendas.models import *


class ItemPedidoInline(admin.TabularInline):
    model = ItemDoPedido
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'numero', 'valor', 'nfe_emitida', 'get_total')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__last_name', 'pessoa__doc__num_doc')
    list_filter = ('numero', 'desconto', 'nfe_emitida')
    raw_id_fields = ('pessoa',)
    actions = (nfe_true, nfe_false)
    inlines = (ItemPedidoInline,)

    Venda.get_total.short_description = 'Total'

    # def total(self,obj):
    #     return obj.get_total()
    # total.short_description = 'Total'


class ItemDoPedidoAdmin(admin.ModelAdmin):
    list_display = ('venda', 'produto', 'quantidade')


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido, ItemDoPedidoAdmin)
