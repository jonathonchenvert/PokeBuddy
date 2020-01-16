# from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Pokemon
from .forms import PokemonForm  # , StatsForm, AttacksForm, OriginalTrainerForm

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView


# Create your views here.

def index(request):
    template_name = 'PokeTraining/index.html'
    all_pokemon_list = Pokemon.objects.order_by('pkmn_number')
    context = {
        'all_pokemon_list': all_pokemon_list
    }

    return render(request, template_name, context)


def new_pokemon(request):
    template_name = 'PokeTraining/new_pokemon.html'

    pokemon_form = PokemonForm(request.POST or None)

    if request.method == "POST" and pokemon_form.is_valid():

        pokemon_form.save()
        # stats_form = StatsForm(data=request.POST)
        # attacks_form = AttacksForm(data=request.POST)
        # ot_form = OriginalTrainerForm(data=request.POST)

        #if pokemon_form.is_valid():
         #   pokemon_form.save()
            # pokemon.stats = stats_form.save()
            # pokemon.attacks = attacks_form.save()
            # pokemon.ot = ot_form.save()

            # stats = stats_form.save(commit=False)
            # attacks = attacks_form.save(commit=False)
            # ot = ot_form.save(commit=False)
            #
            # stats.stats = pokemon
            # stats.save()
            #
            # attacks.attacks = pokemon
            # attacks.save()
            #
            # ot.ot = pokemon
            # ot.save()

        return redirect('/')
        # stats_form = StatsForm()
        # attacks_form = AttacksForm()
        # ot_form = OriginalTrainerForm()

    context = {
        'pokemon_form': pokemon_form,
    }

    # args['stats_form'] = stats_form
    # args['attacks_form'] = attacks_form
    # args['ot_form'] = ot_form

    return render(request, template_name, context)


class Index(generic.ListView):
    model = Pokemon
    context_object_name = 'pokemon'
    template_name = 'PokeTraining/index.html'


class PokemonAddView(BSModalCreateView):
    template_name = 'PokeTraining/add_pkmn.html'
    form_class = PokemonForm
    success_message = 'Success! Pokemon has been added.'
    success_url = reverse_lazy('PokeTraining:index')


class PokemonUpdateView(BSModalUpdateView):
    model = Pokemon
    template_name = 'PokeTraining/edit_pkmn.html'
    form_class = PokemonForm
    success_message = 'Success! Pokemon has been updated.'
    success_url = reverse_lazy('PokeTraining:index')
