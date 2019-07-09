from django.urls import path

from . import views

app_name = 'PokeTraining'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.new_pokemon, name='new_pokemon'),
]
