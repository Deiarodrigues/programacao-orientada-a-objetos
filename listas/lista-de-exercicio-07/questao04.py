class Caneta:

	def __init__(self,cor,marca,numero_ponta,volume_tinta):
		self.cor = cor
		self.marca = marca
		self.numero_ponta = numero_ponta
		self.volume_tinta = volume_tinta

	def encher_caneta (self):
		self.volume_tinta
		return self.volume_tinta

	def escrever(self,escrevendo):
		print(escrevendo)
		self.volume_tinta -=1

	def retornar_marca(self):
		self.marca
		return self.marca

	def caracteristicas(self):
		print(f'Caracteristicas de uma caneta:\nCor; {self.cor}\nMarca; {self.marca}\nNumero da ponta; {self.numero_ponta}\nVolume da tinta; {self.volume_tinta}')

c1 = Caneta("Preta","Bic",0.7,50)
#x = c1.encher_caneta()
#print(f'volume de tinta = {x}')
c1.escrever("ola")
y = c1.retornar_marca()
print(f'A marca e {y}')
c1.caracteristicas()