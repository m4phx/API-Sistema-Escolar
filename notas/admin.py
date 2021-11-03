from django.contrib import admin
from notas.models import Nota


class Notas(admin.ModelAdmin):
    list_display = ['aluno', 'valor']
    list_display_links = ['aluno', 'valor']
    search_fields = ['aluno',]
    list_per_page = 20

admin.site.register(Nota, Notas)