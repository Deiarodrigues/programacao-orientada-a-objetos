import random
nomes = ["Ana","Maria","Julia","Sara"]
sobrenome = ["Lima","Gomes","Vitor","Silva"]

numero = int(input("digite quantos nomes voce quer: "))
with open("texto.txt","w") as saida:
    for linha in range(1,numero+1):
	    tamanho_nomes = random.randint(0,len(nomes)-1)
	    tamanho_sobrenome = random.randint(0,len(sobrenome)-1)
	    idade = random.randint(0,99)
	    nome_gerado = nomes[tamanho_nomes]
	    sobrenome_gerado = sobrenome[tamanho_sobrenome]
	    print("{} {} {} anos".format(nome_gerado,sobrenome_gerado,idade),file = saida)