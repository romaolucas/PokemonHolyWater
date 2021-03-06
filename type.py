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
	type_matrix =[[1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
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

def get_multiplier(atker, atk_type, defender):
	"""Calcula o multiplicador de efetividade de um ataque em um Pokémon"""
	ans = 1.0

	if (atk_type is atker.typ1) or (atk_type is atker.typ2):
		ans = ans * 1.5 # aplicando STAB (Same Type Attack Bonus)

	ans = ans * Type.type_matrix.value[atk_type.value][defender.typ1.value]
	ans = ans * Type.type_matrix.value[atk_type.value][defender.typ2.value]
	
	return ans