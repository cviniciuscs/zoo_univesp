from django.contrib import admin
from apps.biblioteca.models import Livro

class ListandoLivros(admin.ModelAdmin):
    list_display = ('id', 'animal', 'legenda', 'categoria', 'publicada')
    list_display_links = ('id', 'animal')
    search_fields = ('animal','id')
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10
    
    
admin.site.register(Livro, ListandoLivros)
