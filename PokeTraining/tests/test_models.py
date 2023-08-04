from django.test import TestCase
from PokeTraining.models import Pokemon, Attacks, Stats, OriginalTrainer


def setUpModule():
    # Create objects for all classes to use
    Pokemon.objects.create(
        pkmn_name='Charizard',
        pkmn_nickname='リザードン',
        pkmn_number=6,
        pkmn_level=50,
        pkmn_type1='FIRE',
        pkmn_type2='FLYING',
        pkmn_gender='F',
        pkmn_language='ENGLISH',
        ball_captured='BEAST',
        original_generation='1',
        ability='BLAZE',
        nature='ADAMANT'
    )
    OriginalTrainer.objects.create(
        ot=Pokemon.objects.get(pkmn_name='Charizard'),
        pkmn_ot='Me',
        trainer_id=928479,
    )

def tearDownModule():
    pass


class PokemonTestCase(TestCase):
    
    def test_pokemon(self):
        charizard = Pokemon.objects.get(pkmn_name='Charizard')
        self.assertTrue(isinstance(charizard, Pokemon), "Charizard should be a Pokemon")

        self.assertEqual(charizard.pkmn_nickname, 'リザードン', "The Charizard's nickname should be 'リザードン'")
        self.assertEqual(charizard.pkmn_number, 6, "Charizard should have the Pokedex entry 6.")
        self.assertEqual(charizard.pkmn_level, 50, "Charizard should be set to level 50")
        self.assertEqual(charizard.pkmn_type1, 'FIRE', "")
        self.assertEqual(charizard.pkmn_type2, 'FLYING', "")
        self.assertEqual(charizard.pkmn_gender, 'F', "")
        self.assertEqual(charizard.pkmn_language, 'ENGLISH', "")
        self.assertEqual(charizard.ball_captured, 'BEAST', "")
        self.assertEqual(charizard.original_generation, '1', "")
        self.assertEqual(charizard.ability, 'BLAZE', "")
        self.assertEqual(charizard.nature, 'ADAMANT', "Charizard's nature should be 'Adamant'")
        self.assertEqual(str(charizard), charizard.pkmn_name, "Charizard's name should be in __str__")

        self.assertFalse(charizard.pkrs, "Charizard should not have Pokerus")
        self.assertFalse(charizard.shiny, "Charizard should not be shiny (though I wish)")
        self.assertFalse(charizard.ev_trained, "Charizard should not be EV trained")

    def test_pokemon_does_not_exist(self):
        with self.assertRaises(Pokemon.DoesNotExist):
            Pokemon.objects.get(pkmn_name='Lickitung')
        

class AttacksTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls._attacks = Attacks.objects.create(
            attacks=Pokemon.objects.get(pkmn_name='Charizard'),
            attack1='Flamethrower',
            attack2='Belly Drum',
            attack3='Dragon Claw',
            attack4='Earthquake',
        )

        cls._pokemon = Pokemon.objects.get(pkmn_name='Charizard')

    def test_attacks(self):
        self.assertTrue(isinstance(self._attacks, Attacks), "Attacks should be an 'Attacks' object")

        self.assertEqual(
            str(self._attacks), 
            f"(OT ID: {self._pokemon.originaltrainer.trainer_id}) {self._pokemon.pkmn_name}'s Attacks", 
            "Hmm"
        )

class StatsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls._pokemon = Pokemon.objects.get(pkmn_name='Charizard')
        cls._stats = Stats.objects.create(
            stats=cls._pokemon,
            ev_hp=252,
            ev_atk=252,
            ev_def=0,
            ev_satk=0,
            ev_sdef=0,
            ev_spd=6,
            iv_hp=0,
            iv_atk=0,
            iv_def=0,
            iv_satk=0,
            iv_sdef=0,
            iv_spd=0,
        )

    def test_stats(self):
        self.assertTrue(isinstance(self._stats, Stats), "The generated _stats should be of type Stats")

        self.assertEqual(
            str(self._stats), 
            f"(OT ID: {self._pokemon.originaltrainer.trainer_id}) {self._pokemon.pkmn_name}'s Stats",
            "String formatting should match what is defined in models."
        )

class OriginalTrainerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls._pokemon = Pokemon.objects.get(pkmn_name='Charizard')
        cls._original_trainer = OriginalTrainer.objects.get(ot=cls._pokemon)
    
    def test_original_trainer(self):
        self.assertTrue(isinstance(self._original_trainer, OriginalTrainer), "The original trainer subobject should be an instance of OriginalTrainer")

        self.assertEqual(
            str(self._original_trainer),
            f"({self._pokemon.pkmn_name}) Pokemon Trainer: {self._original_trainer.pkmn_ot}\nTrainer ID: {self._original_trainer.trainer_id}",
            "String formatting should match what is defined in models."
        )
