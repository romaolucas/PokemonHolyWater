from flask import Flask, request, abort
from pokemon import Pokemon
from lxml import etree

app = Flask(__name__)

class Server():

    _poke_cliente = None

    @property
    def poke_cliente(self):
        return self._poke_cliente

    @poke_cliente.setter
    def poke_cliente(self, value):
        self._poke_cliente = value

    def startBattle(self):
        try:
            self.poke_cliente = Pokemon(request.data, xml = True) # tratar erro aqui?
            
        except etree.XMLSyntaxError as e:
            print('Erro de sintaxe no XML: ', e)
            abort(422)

        name = input()
        print(name)
        poke_server = Pokemon(name)
        xml = poke_server.toXML(request.data)
        input('escolha o ataque:')
        return xml, 200
     
    def computeAttack(self, id):
        print('Voce escolheu o ataque: ', self.poke_cliente.atks[id].name)
        return 'GGWP', 200

serv = Server()

app.add_url_rule('/battle/', 'startBattle', serv.startBattle, methods=['POST'])
app.add_url_rule('/battle/attack/<int:id>', 'computeAttack', serv.computeAttack,  methods=['POST'])

if __name__ == '__main__':
    app.run(debug = True)

