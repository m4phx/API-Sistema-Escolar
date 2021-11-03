from django.contrib import admin
from cursos.models import Curso


class Cursos(admin.ModelAdmin):
    list_display = ['id', 'codigo_curso', 'descricao']
    list_display_links = ['id', 'codigo_curso']
    search_fields = ['codigo_curso']


admin.site.register(Curso, Cursos)