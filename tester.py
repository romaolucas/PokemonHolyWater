from type import *
from pokemon import *
from attack import *
from battle import *
import unittest

class TestPokemon(unittest.TestCase):

    def setUp(self):
        self.poke = Pokemon('squirtle')
        self.poke2 = Pokemon('charmander')
        self.poke3 = Pokemon('hypno')
        self.poke4 = Pokemon('hitmonlee')
        self.first = Pokemon('ditto')
        self.second = Pokemon('magikarp')
        self.battle = Battle()

    def teste_poke_creation(self):
        self.assertEqual(self.poke.typ1.name, 'water')
        self.assertEqual(self.poke.hp, 50)
        self.assertRaises(IndexError, lambda: self.poke.atks[5])

    def test_attack(self):
        for atk in self.poke.atks:
            atk.pp = 0
        self.assertTrue(self.poke.hasToStruggle())
        self.assertEqual(getMultiplier(self.poke, Type(10), self.poke2), 3.0)
        self.assertEqual(getMultiplier(self.poke4, Type(1), self.poke3), 0.75)

    def test_battle(self):
        self.assertEqual(self.battle.getFirst(self.first, self.second), self.second)
        self.assertFalse(self.battle.willHit(0))
        self.assertAlmostEqual(self.battle.getCrit(512, 7), 19/12)
        mult = getMultiplier(self.poke, self.poke.atks[0].typ, self.poke2)
        crit = self.battle.getCrit(self.poke.spd, self.poke.level)
        self.assertGreaterEqual(self.battle.getDmg(self.poke, self.poke2, 
            self.poke.atks[0], mult, crit), 14.46 )
        self.assertLessEqual(self.battle.getDmg(self.poke, self.poke2, 
            self.poke.atks[0], mult, crit), 68.0)

if __name__ == '__main__':
    unittest.main()
