from type import Type

class Attack:
	name = None
	typ = None
	accu = None
	pwr = None
	pp = None
	maxpp = None
	special = None

	def __init__(self, name, typ, accu, pwr, pp):
		self.name = name
		self.typ = typ
		self.accu = accu
		self.pwr = pwr
		self.pp = pp
		self.maxpp = pp

		if (self.typ.name == 'normal' or self.typ.name == 'fighting' or self.typ.name == 'flying' or self.typ.name == 'ground'  or self.typ.name == 'rock'  or self.typ.name == 'bug' or self.typ.name == 'ghost' or self.typ.name == 'poison'):
			self.special = False
		else:
			self.special = True

	def hasPP(self):
		return self.pp > 0 and not(self.pp is None)
	
