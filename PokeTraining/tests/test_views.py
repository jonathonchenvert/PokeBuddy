from django.test import TestCase
from django.urls import reverse
from PokeTraining.models import Pokemon, OriginalTrainer


def setUpModule():
    # Create objects for all classes to use
    Pokemon.objects.create(
        pkmn_name='Chandelure',
        pkmn_nickname='샹델라', # Korean name for it
        pkmn_number=609,
        pkmn_level=50,
        pkmn_type1='GHOST',
        pkmn_type2='FIRE',
        pkmn_gender='M',
        pkmn_language='ENGLISH',
        ball_captured='BEAST',
        original_generation='5',
        ability='INFILTRATOR',
        nature='TIMID'
    )
    OriginalTrainer.objects.create(
        ot=Pokemon.objects.get(pkmn_name='Chandelure'),
        pkmn_ot='Billy',
        trainer_id=821704,
    )


def tearDownModule():
    pass


class PokemonIndexViewTests(TestCase):
    def test_presence(self):
        response = self.client.get(reverse('PokeTraining:index')) # derived from template name in views.py
        self.assertEqual(response.status_code, 200, "Response code should be 200")
        # print(response.content)
        # self.assertContains(response, "A pokemon should be available")
    
