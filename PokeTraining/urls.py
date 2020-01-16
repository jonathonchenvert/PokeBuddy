from django.urls import path

from . import views

app_name = 'PokeTraining'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('add/', views.new_pokemon, name='new_pokemon'),
]
