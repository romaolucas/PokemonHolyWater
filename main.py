from os import sys
from battle import *
from pokemon import *

#input dos pokemons participantes
argv = sys.argv
first = Pokemon(argv[1])
second = Pokemon(argv[2])

startBattle(first, second)
