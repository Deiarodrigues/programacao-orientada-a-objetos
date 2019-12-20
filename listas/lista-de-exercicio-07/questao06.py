class Retangulo:
    def __init__(self, lado_a,lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_valor_lado(self,novo_valor_a,novo_valor_b):
        self.lado_a = novo_valor_a = int(input("trocar valor ladoA: "))
        self.lado_b = novo_valor_b = int(input("trocar valor ladoB: "))
        
    def retornar_valor_lado(self):
        return self.lado_a
        return self.lado_b

    def calcular_area(self):
        return self.lado_a*self.lado_b
    
    def calcular_perimetro(self):
        return self.lado_a*2+(self.lado_b*2)

    def imprimir (self):
        print(f'metros quadrados de piso: {self.calcular_area()} metros quadrados\nmetros de rodapé: {self.calcular_perimetro()} metros')


ladoA = int(input("ladoA: "))
ladoB = int(input("ladoB: "))
retangulo = Retangulo(ladoA,ladoB)
retangulo.imprimir()