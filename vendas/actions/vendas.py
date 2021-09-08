def nfe_true(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)
nfe_true.short_description = 'NF-e emitida'

def nfe_false(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)
nfe_false.short_description = 'NF-e não emitida'
