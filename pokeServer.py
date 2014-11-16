from flask import Flask, request, abort
from pokemon import Pokemon
from lxml import etree

app = Flask(__name__)

@app.route('/battle/', methods = ['POST'])
def startBattle():
    try:
        poke_cliente = Pokemon(request.data, xml = True) # tratar erro aqui?

    except etree.XMLSyntaxError as e:
        print('Erro de sintaxe no XML: ', e)
        abort(422)

    name = input()
    print(name)
    poke_server = Pokemon(name)
    xml = poke_server.toXML(request.data)
    input('escolha o ataque:')
    return xml, 200
 
@app.route('/battle/attack/<int:id>', methods = ['POST'])
def computeAttack(id):
    print('Voce escolheu o ataque: ',id)
    return 'GGWP', 200

if __name__ == '__main__':
    app.run(debug = True)

