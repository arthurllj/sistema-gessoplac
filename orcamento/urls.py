from django.urls import path
from . import views
from .views import gerar_pdf

urlpatterns = [
    path('', views.index, name='index'),
    path('orcamento/', views.calcular_orcamento, name='orcamento'),
    path('produtos/', views.produtos, name='produtos'),
    path('localizacao/', views.localizacao, name='localizacao'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path( 'gerar-pdf/', gerar_pdf, name='gerar_pdf'),
]

