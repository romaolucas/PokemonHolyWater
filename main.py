from os import sys
from battle import *
from pokemon import *

argv = sys.argv

if len(argv) < 2 or len(argv) > 3:
    print('Erro! Indique o modo de operação (servidor ou cliente) pela linha de'
          ' comando e ou dê o nome de um arquivo com o Pokémon a ser usado ou '
          ' digite os dados do Pokémon pela entrada padrão, linha por linha.')

if argv[1] == 'cliente':
    import client

elif argv[1] == 'servidor':
    import pokeServer
    pokeServer.app.run(debug = True)