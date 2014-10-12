#to ligado que se pa esses import tem alguns redundantes (se pa, n manjo)
import copy
from type import Type
from attack import *

class Pokemon:

	def __init__(self, x): 		#read pokefile
		pokefile = open(x + ".poke")
		pokefile.readline() #primeira linha reservada pra comentários
		stats = pokefile.readline().split(',')
		self.name = stats[0]
		self.level = int(stats[1])
		self.typ1 = Type(int(stats[2]))
		self.typ2 = Type(int(stats[3]))
		self.hp = int(stats[4])
		self.maxhp = self.hp
		self.atk = int(stats[5])
		self.dfs = int(stats[6])
		self.spd = int(stats[7])
		self.spc = int(stats[8])
		self.atks = [None] * 4
		for i in range(0,4):
			atk = pokefile.readline().split(',')
			if (len(atk) != 5):
				continue
			self.atks[i] = Attack(atk[0], Type(int(atk[1])), int(atk[2]), int(atk[3]), int(atk[4]))
		pokefile.close()

	def showStats(self):
		print('Name: ' + self.name + ' Lv' + str(self.level))
		print('HP: ' + str(self.hp) + '/' + str(self.maxhp))
		print('ATK: ' + str(self.atk))
		print('DEF: ' + str(self.dfs))
		print('SPD: ' + str(self.spd))
		print('SPC: ' + str(self.spc))

	def hasToStruggle(self):#checar se vai usar struggle ou não
		struggle = 4
		for atk in self.atks:
			if (atk is None or atk.pp <= 0):
				struggle -= 1
		if (struggle == 0):
			return True
		return False
		

	
	
