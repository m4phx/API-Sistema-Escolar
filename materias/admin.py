from django.contrib import admin
from materias.models import Materia


class Materias(admin.ModelAdmin):
    list_display = ['id', 'nome', 'carga_horaria']
    list_display_links = ['id', 'nome', 'carga_horaria']
    search_fields = ['id', 'nome']


admin.site.register(Materia, Materias)