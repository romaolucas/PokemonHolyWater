import sys
from pokemon import Pokemon
from battle import Battle
from ai import *
 
poke2 = Pokemon("squirtle")
poke1 = Pokemon("charmander")
ai = AI()
battle = Battle()


active = battle.get_first(poke1, poke2)
while battle.all_alive(poke1, poke2):
    
    if (active == poke2):
        AI_choice = battle.make_choice(poke2, poke1, ai)
        battle.attack(poke2, poke1, AI_choice)
    else :
        AI_choice = battle.make_choice(poke1, poke2, ai)
        battle.attack(poke1, poke2, AI_choice)
        
    if (active == poke1): active = poke2
    else : active = poke1

