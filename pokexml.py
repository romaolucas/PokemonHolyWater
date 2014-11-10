# Pra usar:
# python3 pokexml.py pokemon teste.xml
#
# pokemon é um dos arquivos .poke (passado sem a extensão, que nem no programa
# principal) e o teste.xml tem o <battle_state></battle_state> só
#
# O resultado fica num nome_do_pokemon.xml

from pokemon import Pokemon
import sys
import xml.etree.ElementTree as ET

poke1 = Pokemon(sys.argv[1])

tree = ET.parse(sys.argv[2])
root = tree.getroot()

poke    = ET.SubElement(root, 'pokemon')
name    = ET.SubElement(poke, 'name')
lvl     = ET.SubElement(poke, 'level')
attribs = ET.SubElement(poke, 'attributes')
hp      = ET.SubElement(attribs, 'health')
atk     = ET.SubElement(attribs, 'attack')
defense = ET.SubElement(attribs, 'defense')
speed   = ET.SubElement(attribs, 'speed')
special = ET.SubElement(attribs, 'special')
type1   = ET.SubElement(poke, 'type')
type2   = ET.SubElement(poke, 'type')

name.text    = poke1.name
lvl.text     = str(poke1.level)
hp.text      = str(poke1.hp)
atk.text     = str(poke1.atk)
defense.text = str(poke1.dfs)
speed.text   = str(poke1.spd)
special.text = str(poke1.spc)
type1.text   = str(poke1.typ1.value)
type2.text   = str(poke1.typ2.value)

i = 1
for atk in poke1.atks:
    
    attk  = ET.SubElement(poke, 'attacks')
    atkid = ET.SubElement(attk, 'id')
    name  = ET.SubElement(attk, 'name')
    typ   = ET.SubElement(attk, 'type')
    pwr   = ET.SubElement(attk, 'power')
    acc   = ET.SubElement(attk, 'accuracy')
    pp    = ET.SubElement(attk, 'power_points')

    atkid.text = str(i) 
    name.text  = atk.name
    typ.text   = str(atk.typ.value)
    pwr.text   = str(atk.pwr)
    acc.text   = str(atk.accu)
    pp.text    = str(atk.pp)    # considerando o PP atual, não o max

    i += 1

tree.write(poke1.name + '.xml')