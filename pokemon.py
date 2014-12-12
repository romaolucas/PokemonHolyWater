import sys
from lxml import etree
from type import *
from attack import *

class Pokemon:

    def __init__(self, arq, xml = False):
            
        if not xml:

            if arq != sys.stdin:
                # o argumento na linha de comando é o nome do arquivo sem '.poke'
                arq = open("bill-pc/"+ arq + ".poke")

            self.name = arq.readline().strip()
            self.level = int(arq.readline())
            self.hp = int(arq.readline())
            self.maxhp = self.hp
            self.atk = int(arq.readline())
            self.dfs = int(arq.readline())
            self.spd = int(arq.readline())
            self.spc = int(arq.readline())
            self.typ1 = Type(int(arq.readline()))
            self.typ2 = Type(int(arq.readline()))
            natks = int(arq.readline())

            self.atks = []
            for i in range(natks):
                self.atks.append(Attack(arq.readline().strip(),
                        Type(int(arq.readline())), int(arq.readline()),
                        int(arq.readline()), int(arq.readline())))
            
            if arq != sys.stdin:
                arq.close()

        else:

            xsd = open('pokemon.xsd', 'rb')
            schema_root = etree.XML(xsd.read())
            xsd.close()
            schema = etree.XMLSchema(schema_root)
            parser = etree.XMLParser(schema = schema)
            # arq é uma STRING com o XML
            root = etree.fromstring(arq, parser)
            poke = root[0]
            stats = root[0].find('attributes')

            self.name = poke.find('name').text
            self.level = int(poke.find('level').text)
            self.hp = int(stats.find('health').text)
            self.maxhp = self.hp
            self.atk = int(stats.find('attack').text)
            self.dfs = int(stats.find('defense').text)
            self.spd = int(stats.find('speed').text)
            self.spc = int(stats.find('special').text)
            self.typ1 = Type(int(poke.findall('type')[0].text))

            try:    
                self.typ2 = Type(int(poke.findall('type')[1].text))
            
            except IndexError:
                self.typ2 = Type(16)

            self.atks = []

            for atk in poke.findall('attacks'):
                self.atks.append(Attack(
                                        atk.find('name').text,
                                        Type(int(atk.find('type').text)),
                                        int(atk.find('accuracy').text),
                                        int(atk.find('power').text),
                                        int(atk.find('power_points').text)))

    def show_stats(self):
        """Mostra os stats do Pokémon"""
        print('Nome: ' + self.name + ', LVL: ' + str(self.level))
        print('HP: ' + str(self.hp) + '/' + str(self.maxhp))
        print('ATK: ' + str(self.atk))
        print('DEF: ' + str(self.dfs))
        print('SPD: ' + str(self.spd))
        print('SPC: ' + str(self.spc))

    def has_to_struggle(self):
        """Determina se o Pokémon tem que usar Struggle ou não"""
        for atk in self.atks:
            if atk.has_PP():
                return False
        
        return True
            
    def show_atks(self, detail = False):
        """Mostra os ataques do Pokémon (sem detalhes por default)"""
        i = 0
        for attack in self.atks:
            print(str(i+1) + ' - ' + attack.show(detail))
            i += 1

    def to_XML(self, xml):
        """
        Recebe um XML (como uma string) representando um objeto battle_state e
        adiciona nele um elemento pokemon correspondente ao Pokémon que chamou
        o método. Retorna o XML modificado.
        """
        root = etree.fromstring(xml)

        if root.tag != 'battle_state':
            print('Erro no formato do XML')
            sys.exit()

        poke    = etree.SubElement(root, 'pokemon')
        name    = etree.SubElement(poke, 'name')
        lvl     = etree.SubElement(poke, 'level')
        attribs = etree.SubElement(poke, 'attributes')
        hp      = etree.SubElement(attribs, 'health')
        atk     = etree.SubElement(attribs, 'attack')
        defense = etree.SubElement(attribs, 'defense')
        speed   = etree.SubElement(attribs, 'speed')
        special = etree.SubElement(attribs, 'special')
        type1   = etree.SubElement(poke, 'type')
        type2   = etree.SubElement(poke, 'type')

        name.text    = self.name
        lvl.text     = str(self.level)
        hp.text      = str(self.hp)
        atk.text     = str(self.atk)
        defense.text = str(self.dfs)
        speed.text   = str(self.spd)
        special.text = str(self.spc)
        type1.text   = str(self.typ1.value)
        type2.text   = str(self.typ2.value)

        i = 1
        for atk in self.atks:
            
            attk  = etree.SubElement(poke, 'attacks')
            atkid = etree.SubElement(attk, 'id')
            name  = etree.SubElement(attk, 'name')
            typ   = etree.SubElement(attk, 'type')
            pwr   = etree.SubElement(attk, 'power')
            acc   = etree.SubElement(attk, 'accuracy')
            pp    = etree.SubElement(attk, 'power_points')

            atkid.text = str(i) 
            name.text  = atk.name
            typ.text   = str(atk.typ.value)
            pwr.text   = str(atk.pwr)
            acc.text   = str(atk.accu)
            pp.text    = str(atk.pp)    # considerando o PP atual, não o max

            i += 1

        return etree.tostring(root, encoding = 'unicode')