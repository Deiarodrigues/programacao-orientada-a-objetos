class Computador:
	def __init__(self,marca,modelo,componentes,anos_uso,cor):
		self.marca = marca
		self.modelo = modelo
		self.componentes =componentes
		self.anos_uso = anos_uso
		self.cor = cor

	def mostrarMarca(self):
		print(f'{self.marca}')


	def adicionarComponentes(self,novo_comp):
		self.componentes.append(novo_comp)

	def mostrarComponentes(self):
		print(f'{self.componentes}')

	def mostrarAnos(self):
		if self.anos_uso <6:
			print(f'{self.anos_uso}')
		elif self.anos_uso >=6:
			print("Seu Computador esta tao velho que tem problemas de juntas")

	def envelhecer(self):
		self.anos_uso+=1


c = Computador("samsung","intel",["teclado","mouse","cpu","registradores"],5,"branco")
c.mostrarMarca()
c.mostrarAnos()
c.adicionarComponentes("processador")
c.mostrarComponentes()