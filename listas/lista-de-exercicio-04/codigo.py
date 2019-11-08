with open("amazon.csv") as arquivo:
	questao_1 = (0)
	questao_2 = (0)
	questao_3 = (0)
	questao_4 = (0)

	for linha in arquivo:
		linha.strip("")
		ano,estado,mes,numero,data = linha.split(",")
		numero = numero.replace(".","")

		if '"Acre"' == estado and "2015" == ano:
			questao_1 += int(numero)

		elif '"Ceara"' == estado and "2014" == ano:
			questao_2 += int(numero)

		elif '"Amazonas"' == estado:
			questao_3 += int(numero)

		if ano == '"year"':
			continue

		elif int(ano) >= 2010 and '"Mato Grosso"' == estado:
			questao_4 += int(numero)

print("Questão 1:\n No Acre ocorreram {} queimadas em 2015".format(questao_1))
print("\n")
print("Questão 2:\n No Ceará ocorreram {} queimadas em 2014".format(questao_2))
print("\n")
print("Questão 3:\n Ocorreram {} queimadas no estado do Amazonas".format(questao_3))
print("\n")
print("Questão 4:\n De 2010 até o último ano disponível ocorreram {} queimadas no estado Mato Grosso".format(questao_4))