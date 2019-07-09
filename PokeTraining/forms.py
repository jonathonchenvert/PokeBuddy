from django.forms import ModelForm

from .models import Pokemon, Stats, Attacks, OriginalTrainer


class PokemonForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'


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
