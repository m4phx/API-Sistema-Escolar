from django.contrib import admin
from django.urls import path, include
from alunos.views import AlunoViewSet
from cursos.views import CursoViewSet
from esportes.views import EsporteViewSet
from materias.views import MateriaViewSet
from notas.views import NotaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('esportes', EsporteViewSet, basename='Esportes')
router.register('materias', MateriaViewSet, basename='Materias')
router.register('notas', NotaViewSet, basename='Notas')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
