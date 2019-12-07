import random
nomes = ["Ana","Maria","Jose","Henrique","Fatima","Carlos","Andre","Joana","Gustavo","Valmir","Marcos","Alice","Julia"]
sobrenome = ["Silva","Moreira","Lino","Rodrigues","Lima","Gomes","Vitor","Lopes","Sena","Nunes","Marques","Ramos","Borges"]
n = int(input("digite quantas vezes voce quer os nomes: "))
with open ("texto.txt", "w") as saida:
    for i in range (1,n+1):
        tamanho_nomes = random.randint(0,len(nomes)-1)
        tamanho_sobrenome = random.randint(0,len(sobrenome)-1)
        nome_gerado = nomes[tamanho_nomes]
        sobrenome_gerado = sobrenome[tamanho_sobrenome]
        idade = random.randint(0,99)
        altura =random.randint(100,200)
        recebe_altura = altura/100
        print("{} {} {} anos {} m".format(nome_gerado,sobrenome_gerado,idade,recebe_altura),file =  saida)