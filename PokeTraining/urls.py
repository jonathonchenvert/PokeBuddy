from django.urls import path

from . import views

app_name = 'PokeTraining'

urlpatterns = [
    path('', views.index, name='index'),
]
