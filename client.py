import requests
import sys
from pokemon import Pokemon
from lxml import etree
 
poke = Pokemon(sys.argv[1])
 
r = requests.post('http://localhost:5000/battle/', data = poke.toXML(
                                    '<battle_state></battle_state>'))

poke.showAtks()

battle_state = etree.fromstring(r.text)
poke1 = battle_state[0]
battle_state.remove(poke1)
pkmn = etree.tostring(battle_state, encoding = 'unicode')
 
poke2 = Pokemon(pkmn, xml = True)
 
poke2.showStats()
poke2.showAtks()

r = requests.post('http://localhost:5000/battle/attack/1')
print(r.text)
