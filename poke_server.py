from flask import Flask, request, abort
from pokemon import Pokemon
from lxml import etree
from battle import Battle
from ai import *
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

    def start_battle(self):
        try:
            self.poke_cliente = Pokemon(request.data, xml = True)

        except etree.XMLSyntaxError as e:
            print('Erro de sintaxe no XML: ', e)
            abort(422)
        
        if len(sys.argv) == 3:
            poke = Pokemon(sys.argv[2])

        elif len(sys.argv) == 2:
            poke = Pokemon(sys.stdin)

        
        self.poke_server = poke

        battle = Battle()
        ai = AI()

        first = battle.get_first(self.poke_server, self.poke_cliente)

        if first is self.poke_server:
            choice = battle.make_choice(self.poke_server, self.poke_cliente, ai)
            battle.attack(self.poke_server, self.poke_cliente, choice)

            battle.all_alive(self.poke_server, self.poke_cliente)

            xml = self.poke_cliente.to_XML('<battle_state></battle_state>')
            xml = self.poke_server.to_XML(xml)

        else:
            xml = self.poke_server.to_XML(request.data)

        return xml, 200
     
    def compute_attack(self, id):
        
        battle = Battle()
        ai = AI()

        battle.attack(self.poke_cliente, self.poke_server, choice = id - 1)

        print('Oponente escolheu o ataque: ', self.poke_cliente.atks[id - 1].name)

        if battle.all_alive(self.poke_cliente, self.poke_server):
            choice = battle.make_choice(self.poke_server, self.poke_cliente, ai)
            battle.attack(self.poke_server, self.poke_cliente, choice)

        battle.all_alive(self.poke_cliente, self.poke_server)
        battle_state = self.poke_cliente.to_XML('<battle_state></battle_state>')
        battle_state = self.poke_server.to_XML(battle_state)

        return battle_state, 200

    from flask import request

    def shutdown_server(self):
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
        func()

    def shutdown(self):
        self.shutdown_server()
        return 'You have been terminated'

serv = Server()

app.add_url_rule('/battle/', 'start_battle', serv.start_battle, methods=['POST'])
app.add_url_rule('/battle/attack/<int:id>', 'compute_attack', serv.compute_attack,  methods=['POST'])
app.add_url_rule('/shutdown', 'shutdown', serv.shutdown, methods=['POST'])


if __name__ == '__main__':
    app.run(debug = True)