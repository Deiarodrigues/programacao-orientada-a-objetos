class  Pokemon :
    def  __init__ ( self , nome , tipo , descricao , ataques , nivel , poder_luta , brilhante = True):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.ataques = ataques
        self.nivel = nivel
        self.poder_luta = poder_luta
        self.brilhante = brilhante

    def  mostrar_ataques (self):
        self.ataques
        print(f'{self.ataques}')

    def  adicionar_ataque (self ,novos_ataques):
        self.ataques.append(novos_ataques)

    def subir_nivel(self,novo_poder):

        self.nivel+=1
        self.poder_luta.append(novo_poder)

    def  imprimir ( self ):
        print (f'nome: { self.nome } \n tipo: { self.tipo } \n descrição: { self.descricao } \n ataques: { self.ataques } \n nível : { self.nivel } \n poder:{ self.poder_luta } \n é brilhante? { self .brilhante }')

p = Pokemon ( "yanca","ar","passaro",[" ataque sonoro " , " ataque de garras "], 1 , ["canto"], brilhante = True )
p.mostrar_ataques()
p.adicionar_ataque("assas super sonicas")
p.subir_nivel("visao noturna")
p.imprimir()