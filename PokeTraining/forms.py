from django.forms import ModelForm
from .models import Pokemon, Stats, Attacks, OriginalTrainer
import pokebase as pb


class PokemonForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = ['pkmn_name', 'pkmn_nickname', 'pkmn_level', 'pkmn_gender',
                  'ball_captured', 'original_generation', 'nature']

    def save(self, commit=True):
        pokemon = super(PokemonForm, self).save(commit=False)
        entered_pkmn = pb.pokemon(self.cleaned_data['pkmn_name'])
        pokemon.pkmn_name = entered_pkmn.name.capitalize()
        pokemon.pkmn_number = entered_pkmn.id
        pokemon.pkmn_type1 = entered_pkmn.types[0].type.name.upper()
        pokemon.ability = entered_pkmn.abilities[0].ability.name.capitalize()

        try:
            pokemon.pkmn_type2 = entered_pkmn.types[1].type.name.upper()
        except IndexError:
            pass

        if commit:
            pokemon.save()

        return pokemon


class StatsForm(ModelForm):
    class Meta:
        model = Stats
        fields = ('ev_hp', 'ev_atk', 'ev_def',
                  'ev_satk', 'ev_sdef', 'ev_spd',
                  'iv_hp', 'iv_atk', 'iv_def',
                  'iv_satk', 'iv_sdef', 'iv_spd')


class AttacksForm(ModelForm):
    class Meta:
        model = Attacks
        fields = ('attack1', 'attack2', 'attack3', 'attack4')


class OriginalTrainerForm(ModelForm):
    class Meta:
        model = OriginalTrainer
        fields = ('pkmn_ot', 'trainer_id')
