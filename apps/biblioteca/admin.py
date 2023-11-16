from django.contrib import admin
from apps.biblioteca.models import Livro

class ListandoLivros(admin.ModelAdmin):
    list_display = ('id', 'nome', 'especie', 'classe', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome','id')
    list_filter = ('classe',)
    list_editable = ('publicada',)
    list_per_page = 10
    
    
admin.site.register(Livro, ListandoLivros)
