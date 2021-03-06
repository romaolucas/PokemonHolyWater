from type import *
from pokemon import *
from attack import *
from battle import *
import poke_server
import ai
from lxml import etree
from flask import request
import unittest

class Test_Pokemon(unittest.TestCase):

    def setUp(self):
        self.poke = Pokemon('squirtle')
        self.poke2 = Pokemon('charmander')
        self.poke3 = Pokemon('hypno')
        self.poke4 = Pokemon('hitmonlee')
        self.first = Pokemon('ditto')
        self.second = Pokemon('magikarp')
        self.battle = Battle()
        poke_server.app.config['TESTING'] = True
        self.app = poke_server.app.test_client()

    def teste_poke_creation(self):
        self.assertEqual(self.poke.typ1.name, 'water')
        self.assertEqual(self.poke.hp, 50)
        self.assertRaises(IndexError, lambda: self.poke.atks[5])

    def test_attack(self):
        for atk in self.poke.atks:
            atk.pp = 0
        self.assertTrue(self.poke.has_to_struggle())
        self.assertEqual(get_multiplier(self.poke, Type(10), self.poke2), 3.0)
        self.assertEqual(get_multiplier(self.poke4, Type(1), self.poke3), 0.75)

    def test_battle(self):
        self.assertEqual(self.battle.get_first(self.first, self.second), self.second)
        self.assertFalse(self.battle.will_hit(0))
        self.assertAlmostEqual(self.battle.get_crit(512, 7), 19/12)
        mult = get_multiplier(self.poke, self.poke.atks[0].typ, self.poke2)
        crit = self.battle.get_crit(self.poke.spd, self.poke.level)
        self.assertGreaterEqual(self.battle.get_dmg(self.poke, self.poke2, 
            self.poke.atks[0], mult, crit), 14.46 )
        self.assertLessEqual(self.battle.get_dmg(self.poke, self.poke2, 
            self.poke.atks[0], mult, crit), 68.0)

    def test_requests(self):
        test = self.app.post('/battle/', data = {'oi': ' cueio'})
        assert 200 is not test.status_code
        test = self.app.post('/battle/', data = 'magikarp')
        assert 200 is not test.status_code
        test = self.app.post('/battle/', data = '')
        assert 200 is not test.status_code
        self.assertRaises(RuntimeError, self.app.post, '/shutdown')

    def test_ai(self):
        ai = AI("allin")
        self.assertEqual(ai.choose_atk(self.poke, self.poke2, 42), 3, "Ataque escolhido errado (nao eh o mais eficiente no modo 'allin')")
        self.assertEqual(ai.choose_atk(self.poke2, self.poke, 42), 3, "Ataque escolhido errado (nao eh o mais eficiente no modo 'allin')")
        self.assertEqual(ai.choose_atk(self.poke3, self.poke2, 42), 1, "Ataque escolhido errado (nao eh o mais eficiente no modo 'allin')")

        ai.mode = "risky"
        self.assertEqual(ai.choose_atk(self.poke, self.poke2, 80), 3, "Ataque escolhido errado (nao eh o mais eficiente no modo 'risky')")
        self.assertEqual(ai.choose_atk(self.poke, self.poke2, 81), 0, "Ataque escolhido errado (nao eh o mais eficiente no modo 'risky')")
        self.assertEqual(ai.choose_atk(self.poke2, self.poke, 80), 3, "Ataque escolhido errado (nao eh o mais eficiente no modo 'risky')")
        self.assertEqual(ai.choose_atk(self.poke2, self.poke, 81), 2, "Ataque escolhido errado (nao eh o mais eficiente no modo 'risky')")
        self.assertEqual(ai.choose_atk(self.poke3, self.poke2, 31), 1, "Ataque escolhido errado (nao eh o mais eficiente no modo 'risky'")
        self.assertEqual(ai.choose_atk(self.poke3, self.poke2, 51), 1, "Ataque escolhido errado (nao eh o mais eficiente no modo 'risky'")
         
        ai.mode = "safe"
        self.assertEqual(ai.choose_atk(self.poke, self.poke2, 42), 0, "Ataque escolhido errado (nao eh o mais eficiente no modo 'safe')")
        self.assertEqual(ai.choose_atk(self.poke2, self.poke, 42), 2, "Ataque escolhido errado (nao eh o mais eficiente no modo 'safe')")
        self.assertEqual(ai.choose_atk(self.poke3, self.poke2, 42), 1, "Ataque escolhido errado (nao eh o mais eficiente no modo 'safe')")

#Nota: o metodo change_battle_mode muda o modo de batalha do segundo pokemon passado no parametro, ou seja, do defender
        ai.change_battle_mode(self.poke2, self.poke)
        self.assertEqual(ai.mode, "allin", "Modo de batalha errado")
        ai.change_battle_mode(self.poke, self.poke2)
        self.assertEqual(ai.mode, "safe", "Modo de batalha errado")
        ai.change_battle_mode(self.poke2, self.poke3)
        self.assertEqual(ai.mode, "allin", "Modo de batalha errado")

if __name__ == '__main__':
    unittest.main()
