import sys
from type import *
from attack import *

class Pokemon:

	def __init__(self, arq):
		if arq != sys.stdin:
			# o argumento na linha de comando é o nome do arquivo sem '.poke'
			arq = open(arq + ".poke")

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

	def showStats(self):
		"""Mostra os stats do Pokémon"""
		print('Nome: ' + self.name + ', LVL: ' + str(self.level))
		print('HP: ' + str(self.hp) + '/' + str(self.maxhp))
		print('ATK: ' + str(self.atk))
		print('DEF: ' + str(self.dfs))
		print('SPD: ' + str(self.spd))
		print('SPC: ' + str(self.spc))

	def hasToStruggle(self):
		"""Determina se o Pokémon tem que usar Struggle ou não"""
		for atk in self.atks:
			if atk.hasPP():
				return False
		
		return True
		
	def showAtks(self, detail = False):
		"""Mostra os ataques do Pokémon (sem detalhes por default)"""
		i = 0
		for attack in self.atks:
			print(str(i+1) + ' - ' + attack.show(detail))
			i += 1