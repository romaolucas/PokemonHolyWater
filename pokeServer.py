from flask import Flask, request, abort
from pokemon import Pokemon
from lxml import etree
from battle import Battle
import sys

app = Flask(__name__)

class Server():

    _poke_cliente = None
    _poke_server  = None

    @property
    def poke_cliente(self):
        return self._poke_cliente

    @property
    def poke_server(self):
        return self._poke_server

    @poke_cliente.setter
    def poke_cliente(self, value):
        self._poke_cliente = value

    @poke_server.setter
    def poke_server(self, value):
        self._poke_server = value

    def startBattle(self):
        try:
            self.poke_cliente = Pokemon(request.data, xml = True)

        except etree.XMLSyntaxError as e:
            print('Erro de sintaxe no XML: ', e)
            abort(422)

        name = input('Digite o nome do arquivo com o Pokémon que vai usar'
                     ', ou digite stdin se vai entrar com as informações pela'
                     'entrada padrão: ')
        
        if name == 'stdin':
            self.poke_server = Pokemon(sys.stdin)
        else:
            self.poke_server = Pokemon(name)

        battle = Battle()
        first = battle.getFirst(self.poke_server, self.poke_cliente)

        if first is self.poke_server:
            battle.attack(self.poke_server, self.poke_cliente)

            battle.allAlive(self.poke_server, self.poke_cliente)

            xml = self.poke_cliente.toXML('<battle_state></battle_state>')
            xml = self.poke_server.toXML(xml)

        else:
            xml = self.poke_server.toXML(request.data)

        return xml, 200
     
    def computeAttack(self, id):
        
        battle = Battle()
        battle.attack(self.poke_cliente, self.poke_server, choice = id - 1)

        print('Voce escolheu o ataque: ', self.poke_cliente.atks[id - 1].name)

        battle.allAlive(self.poke_cliente, self.poke_server)

        battle.attack(self.poke_server, self.poke_cliente)

        battle.allAlive(self.poke_cliente, self.poke_server)

        battle_state = self.poke_cliente.toXML('<battle_state></battle_state>')
        battle_state = self.poke_server.toXML(battle_state)

        return battle_state, 200

serv = Server()

app.add_url_rule('/battle/', 'startBattle', serv.startBattle, methods=['POST'])
app.add_url_rule('/battle/attack/<int:id>', 'computeAttack', serv.computeAttack,  methods=['POST'])

if __name__ == '__main__':
    app.run(debug = True)