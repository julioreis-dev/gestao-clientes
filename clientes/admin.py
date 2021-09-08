from django.contrib import admin
from clientes.models.clientes import Person, Documento


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'telefone')
    search_fields = ('first_name', )

class DocmentoAdmin(admin.ModelAdmin):
    list_display = ('num_doc',)

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocmentoAdmin)
