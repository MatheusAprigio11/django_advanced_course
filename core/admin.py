from django.contrib import admin

from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)