from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('materiais', views.lista_material, name='lista_material'),
    path('resultado', views.lista_pesquisa, name='lista_pesquisa'),

]


