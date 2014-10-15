import sys
import random
from pokemon import *
from type import *


def allAlive(first, second): #checa condição para o laço de batalha continuar
	if first.hp <= 0 or second.hp <= 0:
		return False
	else:
		 return True

def getFirst(poke1, poke2):
	if (poke1.spd == poke2.spd):
		chance = random.randint(1, 100)
		if (chance < 50):
			return poke1
		else:
			return poke2
	else:
		if (poke1.spd > poke2.spd):
			return poke1
		else:
			return poke2

def effectMessage(mult): #printa message de acordo com efetividade do atk
	if mult <= 0.75 and mult > 0:
		return ' e foi pouco efetivo.'
	elif mult >= 2.0:
		return ' e foi super efetivo!'
	elif mult == 0:
		return ' e não foi efetivo!'
	else:
		return '.'

def getLuck(): #devolve fator random da formula
	luck = random.randint(217, 255)
	luck = luck * 100
	luck = luck / 255
	luck = luck / 100
	return luck

def willHit(accu):
	chance = random.uniform(1, 100)
	if (chance <= accu):
		return True
	else:
		return False

def getCrit(speed):
	critRate = speed*100/512
	chance = random.uniform(1, 100)
	if (chance <= critRate):
		return 2.0
	else:
		return 1.0

def getDmg(active, defender, atk, typeMult, crit): #devolve o dano de um atk
	luck = getLuck()
	#checar tipo do atk
	if (not atk.special):
		offensiveStat = active.atk
		defensiveStat = defender.dfs
	else:
		offensiveStat = active.spc
		defensiveStat = defender.spc
	#calculo do baseDmg
	baseDmg = ((((2*active.level) + 10)/250)*(offensiveStat/defensiveStat)*(atk.pwr)) + 2
	return crit*baseDmg*typeMult*luck


def startBattle(first, second):
	#determinando quem começa
	active = getFirst(first, second)
	if (active is first):
		defender = second
	else:
		defender = first
	result = True

	#laço da batalha
	while(result is True):
		print('vez do ' + active.name + ' HP: ' + str(int(active.hp)) + '/' + str(int(active.maxhp)) + ' LVL: ' + str(active.level))
		active.showAtks()
		choice = int(input('Escolha o ataque de seu pokemon (1-4):\n')) -1

		#processamento da escolha
		if (active.hasToStruggle()):
			a = 2 #substituir pro código do struggle aqui
		elif not(choice in [0, 1, 2, 3]):
			print('Escolha de ataque inválida!')
			continue
		elif (active.atks[choice] is None):
			print('Espaço vazio, escolha outro ataque!')
			continue
		elif (active.atks[choice].pp <= 0):
			print('Sem PP para usar esse ataque!')
			continue
		else:   #efeitos da choice
			active.atks[choice].pp -= 1
			typeMult = getMultiplier(active, active.atks[choice].typ, defender)
			crit = getCrit(active.spd)
			critMsg = ''
			if (crit == 2.0):
				critMsg = ' Foi um ataque crítico!!'
			dmg = getDmg(active, defender, active.atks[choice], typeMult, crit)
			if (willHit(active.atks[choice].accu)):
				defender.hp -= dmg
				print(active.name + ' usou ' + active.atks[choice].name + effectMessage(typeMult) + critMsg)
			else:
				print(active.name + ' usou ' + active.atks[choice].name + ' e errou.')

		#troca de turno
		if (active is first):
			active = second
			defender = first
		else:
			active = first
			defender = second
		result = allAlive(first, second)

	#fim da batalha
	print(active.name + ' desmaiou! ' + defender.name + ' ganhou a luta!')




if __name__ == "__main__":
    sys.exit(main())
