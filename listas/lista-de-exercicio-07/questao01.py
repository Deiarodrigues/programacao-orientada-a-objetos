class Bola:
	def __init__(self,cor,circunferencia,material):
		self.cor = cor
		self.circunferencia = circunferencia
		self.material = material

	def trocarCor(self,novaCor):
		self.cor = novaCor

	def mostrarCor(self):
		print(f'{self.cor}')

	def detalhes(self):
		print(f'{self.circunferencia}\n{self.material}')


b1 = Bola("rosa",3,"plastico")
b1.trocarCor("Roxo")
b1.mostrarCor()
b1.detalhes()