from django.test import TestCase

from PokeTraining.models import Pokemon
from ..forms import PokemonForm


def setUpModule():
    pass

def tearDownModule():
    pass


class PokemonFormTestCase(TestCase):
    def test_add_pokemon_two_types(self):
        cutiefly = {
            'pkmn_name': 'Cutiefly',
            'pkmn_nickname': 'アブリー',
            'pkmn_level': '5',
            'pkmn_gender': 'F',
            'ball_captured': 'LOVE',
            'original_generation': '7',
            'nature': 'MODEST',
        }
        form = PokemonForm(data=cutiefly)
        form.save()

        cutiefly = Pokemon.objects.get(pkmn_name='Cutiefly')
        self.assertTrue(isinstance(cutiefly, Pokemon), "Cutiefly should be a Pokemon")

        self.assertEqual(cutiefly.pkmn_nickname, 'アブリー', "The Cutiefly's nickname should be 'アブリー'")
        self.assertEqual(cutiefly.pkmn_number, 742, "Cutiefly should have the Pokedex entry 742.")
        self.assertEqual(cutiefly.pkmn_level, 5, "Cutiefly should be set to level 5")
        self.assertEqual(cutiefly.pkmn_type1, 'BUG', "Cutiefly's first type should be 'Bug'")
        self.assertEqual(cutiefly.pkmn_type2, 'FAIRY', "Cutiefly's second type should be 'Fairy'")
        self.assertEqual(cutiefly.pkmn_gender, 'F', "Cutiefly should be a female")
        self.assertEqual(cutiefly.pkmn_language, 'ENGLISH', "Cutiefly should have originated from an English game")
        self.assertEqual(cutiefly.ball_captured, 'LOVE', "Cutiefly should have been caught in a Love Ball")
        self.assertEqual(cutiefly.original_generation, '7', "Cutiefly should originally be from generation 7")
        self.assertEqual(cutiefly.ability, 'Honey-gather', "Cutiefly's ability should be 'Honey Gather' as its first ability")
        self.assertEqual(cutiefly.nature, 'MODEST', "Cutiefly's nature should be 'Modest'")
        self.assertEqual(str(cutiefly), cutiefly.pkmn_name, "Cutiefly's name should be in __str__")

        self.assertFalse(cutiefly.pkrs, "Cutiefly should not have Pokerus")
        self.assertFalse(cutiefly.shiny, "Cutiefly should not be shiny (though I wish)")
        self.assertFalse(cutiefly.ev_trained, "Cutiefly should not be EV trained")
    
    def test_add_pokemon_one_type(self):
        greavard = {
            'pkmn_name': 'Greavard',
            'pkmn_nickname': 'Bochi', 
            'pkmn_level': '7',
            'pkmn_gender': 'M',
            'ball_captured': 'BEAST',
            'original_generation': '9',
            'nature': 'JOLLY',
        }
        form = PokemonForm(data=greavard)
        form.save()

        greavard = Pokemon.objects.get(pkmn_name='Greavard')
        self.assertTrue(isinstance(greavard, Pokemon), "Greavard should be a Pokemon")

        self.assertEqual(greavard.pkmn_nickname, 'Bochi', "The Greavard's nickname should be 'Bochi'")
        self.assertEqual(greavard.pkmn_number, 971, "Greavard should have the Pokedex entry 742.")
        self.assertEqual(greavard.pkmn_level, 7, "Greavard should be set to level 5")
        self.assertEqual(greavard.pkmn_type1, 'GHOST', "Greavard's first type should be 'Ghost'")
        self.assertEqual(greavard.pkmn_type2, None, "Greavard should not have a second type")
        self.assertEqual(greavard.pkmn_gender, 'M', "Greavard should be a male")
        self.assertEqual(greavard.pkmn_language, 'ENGLISH', "Greavard should have originated from an English game")
        self.assertEqual(greavard.ball_captured, 'BEAST', "Greavard should have been caught in a Beast Ball")
        self.assertEqual(greavard.original_generation, '9', "Greavard should originally be from generation 7")
        self.assertEqual(greavard.ability, 'Pickup', "Greavard's ability should be 'Pickup' as its first ability")
        self.assertEqual(greavard.nature, 'JOLLY', "Greavard's nature should be 'Jolly'")
        self.assertEqual(str(greavard), greavard.pkmn_name, "Greavard's name should be in __str__")

        self.assertFalse(greavard.pkrs, "Greavard should not have Pokerus")
        self.assertFalse(greavard.shiny, "Greavard should not be shiny (though I wish)")
        self.assertFalse(greavard.ev_trained, "Greavard should not be EV trained")

