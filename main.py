from os import sys
from battle import *
from pokemon import *

argv = sys.argv

# se há dois argumentos de linha de comando, são os arquivos com Pokémons
if len(sys.argv) == 3:
    first = Pokemon(sys.argv[1])
    second = Pokemon(sys.argv[2])

elif len(sys.argv) == 2:
    sys.exit('Erro! Ou dê o nome de dois arquivos ou escreva os detalhes'
            ' dos Pokémons linha por linha na entrada padrão')

# se não há nenhum argumento, leitura é pela entrada padrão,
# sem redirecionamento de arquivo    
elif len(sys.argv) == 1:
    first = Pokemon(sys.stdin)
    second = Pokemon(sys.stdin)

# começa a batalha
Battle().battle(first, second)