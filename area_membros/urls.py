from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/area_membros', views.area_membros, name='area_membros'),
    path('dashboard/area_membros/logar_membro', views.logar_membro, name='logar_membro'),
]