import requests
import sys
from pokemon import Pokemon
from lxml import etree
from battle import Battle
from ai import *

ai = None

if len(sys.argv) == 4:
    ai = AI()

if len(sys.argv) >= 3:
    poke = Pokemon(sys.argv[2])

elif len(sys.argv) == 2:
    poke = Pokemon(sys.stdin)

# começa a bataha


r = requests.post('http://localhost:5000/battle/', data = poke.to_XML(
                                    '<battle_state></battle_state>'))

while r.status_code != 200:
    print('status code: ', r.status_code)
    arq = input('Digite um nome de arquivo valido: ')
    poke = Pokemon(arq)
    r = requests.post('http://localhost:5000/battle/', data = poke.to_XML(
                                    '<battle_state></battle_state>'))

battle = Battle()

poke = Pokemon(r.text, xml = True)

battle_state = etree.fromstring(r.text)
poke1 = battle_state[0]
battle_state.remove(poke1)
pkmn = etree.tostring(battle_state, encoding = 'unicode')
 
poke2 = Pokemon(pkmn, xml = True)
 
while battle.all_alive(poke, poke2):

    atk_id = battle.make_choice(poke, poke2, ai) + 1
    r = requests.post('http://localhost:5000/battle/attack/' + str(atk_id))

    poke = Pokemon(r.text, xml = True)

    battle_state = etree.fromstring(r.text)
    poke1 = battle_state[0]
    battle_state.remove(poke1)
    pkmn = etree.tostring(battle_state, encoding = 'unicode')
 
    poke2 = Pokemon(pkmn, xml = True)

r = requests.post('http://localhost:5000/shutdown')
