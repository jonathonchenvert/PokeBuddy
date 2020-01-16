from django.urls import path

from . import views

app_name = 'PokeTraining'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('add/', views.new_pokemon, name='new_pokemon'),
    # path('add/', views.PokemonAddView.as_view(), name='add_pkmn'),
    path('edit/<int:pk>', views.PokemonUpdateView.as_view(), name='edit_pkmn'),
]
