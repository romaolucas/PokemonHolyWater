import requests
import sys
from pokemon import Pokemon
from lxml import etree
from battle import Battle
 
if len(sys.argv) == 2:
    poke = Pokemon(sys.argv[1])

elif len(sys.argv) == 1:
    poke = Pokemon(sys.stdin)

else:
    sys.exit('Erro! Ou dê o nome de um arquivo ou escreva os detalhes'
            ' do Pokémon linha por linha na entrada padrão')

# começa a bataha
r = requests.post('http://localhost:5000/battle/', data = poke.toXML(
                                    '<battle_state></battle_state>'))

while r.status_code != 200:
    print('status code: ', r.status_code)
    arq = input('Digite um nome de arquivo valido: ')
    poke = Pokemon(arq)
    r = requests.post('http://localhost:5000/battle/', data = poke.toXML(
                                    '<battle_state></battle_state>'))

battle = Battle()

poke = Pokemon(r.text, xml = True)

battle_state = etree.fromstring(r.text)
poke1 = battle_state[0]
battle_state.remove(poke1)
pkmn = etree.tostring(battle_state, encoding = 'unicode')
 
poke2 = Pokemon(pkmn, xml = True)
 
while battle.allAlive(poke, poke2):

    atk_id = battle.make_choice(poke) + 1
    r = requests.post('http://localhost:5000/battle/attack/' + str(atk_id))

    poke = Pokemon(r.text, xml = True)

    battle_state = etree.fromstring(r.text)
    poke1 = battle_state[0]
    battle_state.remove(poke1)
    pkmn = etree.tostring(battle_state, encoding = 'unicode')
 
    poke2 = Pokemon(pkmn, xml = True)