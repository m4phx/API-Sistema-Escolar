from django.contrib import admin
from esportes.models import Esporte


class Esportes(admin.ModelAdmin):
    list_display = ['id', 'nome', 'tipo']
    list_display_links = ['id', 'nome', 'tipo']
    search_fields = ['id']


admin.site.register(Esporte, Esportes)