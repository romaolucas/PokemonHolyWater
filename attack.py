class Attack:
	
	def __init__(self, name, typ, accu, pwr, pp):
		self.name = name
		self.typ = typ
		self.accu = accu
		self.pwr = pwr
		self.pp = pp
		self.maxpp = pp

		if (self.typ.name == 'normal' or self.typ.name == 'fighting'
			or self.typ.name == 'flying' or self.typ.name == 'ground'  
			or self.typ.name == 'rock'  or self.typ.name == 'bug' 
			or self.typ.name == 'ghost' or self.typ.name == 'poison'):
				self.special = False
		else:
			self.special = True

	def has_PP(self):
		"""Determina se um ataque tem PP ou não"""
		return self.pp > 0 and not(self.pp is None)

	def show(self, detail):
		"""Mostra as informações de um ataque com detalhe de acordo com detail"""
		if detail:
			return (self.name + ' - PWR: ' + str(self.pwr) + 
			' - PP restante: ' + str(self.pp) +
			' - ACC: ' + str(self.accu) + ' - TYPE: ' + self.typ.name)

		return self.name + ', PP restante: ' + str(self.pp)