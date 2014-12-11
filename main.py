from os import sys
from battle import *
from pokemon import *

argv = sys.argv

if len(argv) < 2 or len(argv) > 4:
    print('Erro! Modo de execucao nao reconhecido.'
            'Uso: python3 main.py <cliente/servidor> <nome do pokemon> (opcional) <ai> (opcional)'
            'A opcao ai so vale para cliente')

if argv[1] == 'cliente':
    import client

elif argv[1] == 'servidor':
    import poke_server
    poke_server.app.run(debug = True)
