from enum import Enum
class Type(Enum):
	normal = 0
	fighting = 1
	flying = 2
	poison = 3
	ground = 4
	rock = 5
	bird = 6
	bug = 7
	ghost = 8
	fire = 9
	water = 10
	grass = 11
	electric = 12
	psychic = 13
	ice = 14
	dragon = 15
	blank = 16
	typeMatrix =[[1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
		     [2.0, 1.0, 0.5, 0.5, 1.0, 2.0, 0.0, 0.5, 0.0, 1.0, 1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 1.0],
		     [1.0, 2.0, 1.0, 1.0, 1.0, 0.5, 0.0, 2.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0],
		     [1.0, 1.0, 1.0, 0.5, 0.5, 0.5, 0.0, 1.0, 0.5, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0],
		     [1.0, 1.0, 0.0, 2.0, 1.0, 2.0, 0.0, 0.5, 1.0, 2.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0, 1.0],
		     [1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 0.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0],
		     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
		     [1.0, 0.5, 0.5, 0.5, 1.0, 1.0, 0.0, 1.0, 0.5, 0.5, 1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0],
		     [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0],
		     [1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.5, 2.0, 1.0, 1.0, 2.0, 0.5, 1.0],
		     [1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 0.0, 1.0, 1.0, 2.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0],
		     [1.0, 1.0, 0.5, 0.5, 2.0, 2.0, 0.0, 0.5, 1.0, 0.5, 2.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0],
		     [1.0, 1.0, 2.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 2.0, 0.5, 0.5, 1.0, 1.0, 0.5, 1.0],
		     [1.0, 2.0, 1.0, 2.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0],
		     [1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 0.0, 1.0, 1.0, 0.5, 0.5, 2.0, 1.0, 1.0, 0.5, 2.0, 1.0],
		     [1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0]]

def getMultiplier(atker, atkType, defender):
	ans = 1.0
	if (atkType is atker.typ1) or (atkType is atker.typ2):
		ans = ans * 1.5 #aplicando STAB (Same Type Attack Bonus)
	ans = ans * Type.typeMatrix.value[atkType.value][defender.typ1.value]
	ans = ans * Type.typeMatrix.value[atkType.value][defender.typ2.value]
	return ans
	

