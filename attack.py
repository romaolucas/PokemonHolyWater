from type import Type

class Attack:
	name = None
	typ = None
	accu = None
	pwr = None
	pp = None
	maxpp = None

	def __init__(self, name, typ, accu, pwr, pp):
		self.name = name
		self.typ = typ
		self.accu = accu
		self.pwr = pwr
		self.pp = pp
		self.maxpp = pp

	def hasPP(self):
		return self.pp > 0 and not(self.pp is None)
	
