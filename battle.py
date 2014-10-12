import sys
from pokemon import *

argv = sys.argv
first = Pokemon(argv[1])
second = Pokemon(argv[2])

def allAlive():
	if first.hp <= 0 and second.hp <= 0:
		return 'draw'
	elif first.hp <= 0:
		return '1st: ' + first.name
	elif second.hp <= 0:
		return '2nd: ' + second.name
	else:
		 return True

	

def main(argv=None):
	active = first
	while(allAlive()):
		print('vez do ' + active.name)
		for i in range(0, 4):
			print(str(i+1) + '-' + active.atks[i].name + ' - PWR: ' + str(active.atks[i].pwr) + ' - PP: ' + str(active.atks[i].pp))
		choice = input('Escolha o ataque de seu pokemon (1-4):\n')
		#efeitos da choice
		if (active is first):
			active = second
		else:
			active = first



if __name__ == "__main__":
    sys.exit(main())
