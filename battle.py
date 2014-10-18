import sys
import random
import math
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

def getCrit(speed, level):
	critRate = speed*100/512
	chance = random.uniform(1, 100)
	if (chance <= critRate):
		return (2 * level + 5) / (level + 5)
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
	return math.floor(crit * baseDmg * typeMult * luck)


def startBattle(first, second):
	#determinando quem começa
	active = getFirst(first, second)
	if (active is first):
		defender = second
	else:
		defender = first
	result = True

	#laço da batalha
	while (result is True):
		struggle = False
		print('\nvez do ' + active.name + ' HP: ' + str(int(active.hp)) + '/' + str(int(active.maxhp)) + ' LVL: ' + str(active.level))
		active.showAtks()
		choice = int(input('Escolha o ataque de seu pokemon (1-4):\n')) -1

		if (active.hasToStruggle()):
			struggle = True

		#processamento da escolha
		if (not (choice in [0, 1, 2, 3])):
			print('Escolha de ataque inválida!')
			continue
		elif (choice in [0, 1, 2, 3] and len(active.atks) < choice + 1):
			print('Espaço vazio, escolha outro ataque!')
			continue
		elif (active.atks[choice].pp <= 0 and not struggle):
			print('Sem PP para usar esse ataque!')
			continue
		
		else:   #efeitos da choice
			if (struggle):
				attack = Attack('Struggle', Type(0), 100, 50, 10)
			else:
				attack = active.atks[choice]

			if (not struggle):
				attack.pp -= 1

			typeMult = getMultiplier(active, attack.typ, defender)
			crit = getCrit(active.spd, active.level)
			critMsg = ''
			if (crit != 1.0):
				critMsg = ' Foi um ataque crítico!!'
			dmg = getDmg(active, defender, attack, typeMult, crit)

			if (struggle):
				print(active.name + ' não tem mais nenhum ataque sobrando.')

			if (willHit(attack.accu)):
				defender.hp -= dmg
				print(active.name + ' usou ' + attack.name + effectMessage(typeMult) + critMsg)

			else:
				print(active.name + ' usou ' + attack.name + ' e errou.')

			if (struggle):
				active.hp -= dmg / 2
				print(active.name + ' tomou dano de recoil.')

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