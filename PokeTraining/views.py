from django.shortcuts import render

from .models import Pokemon


# Create your views here.
def index(request):
    template_name = 'PokeTraining/index.html'
    all_pokemon_list = Pokemon.objects.order_by('pkmn_number')
    context = {
        'all_pokemon_list': all_pokemon_list
    }

    return render(request, template_name, context)
