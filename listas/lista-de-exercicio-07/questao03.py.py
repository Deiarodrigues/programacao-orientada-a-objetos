class Quadrado:
	def __init__ (self,tamanho_do_lado):
		self.tamanho_do_lado = tamanho_do_lado
		print(f'tamaho do lado = {self.tamanho_do_lado}')

	def mudar_valor(self,novo_valor):
		self.tamanho_do_lado = novo_valor
		
	def retornar_valor(self):
		self.tamanho_do_lado
		return self.tamanho_do_lado

	def calcular_area(self):
		area = self.tamanho_do_lado*self.tamanho_do_lado
		return area


q1 = Quadrado(4)
q1.mudar_valor(5)

x = q1.retornar_valor()
print(f'retornar o novo valor do lado = {x}')
y = q1.calcular_area()
print(f'area do lado = {y}')