import sys
from pokemon import Pokemon
from battle import Battle
from ai import *
 
poke2 = Pokemon("squirtle")
poke1 = Pokemon("charmander")
ai = AI()
battle = Battle()


active = battle.getFirst(poke1, poke2)
while battle.allAlive(poke1, poke2):
    
    if (active == poke2):
        AIchoice = battle.make_choice(poke2, poke1, ai)
        battle.attack(poke2, poke1, AIchoice)
    else :
        AIchoice = battle.make_choice(poke1, poke2, ai)
        battle.attack(poke1, poke2, AIchoice)
        
    if (active == poke1): active = poke2
    else : active = poke1

