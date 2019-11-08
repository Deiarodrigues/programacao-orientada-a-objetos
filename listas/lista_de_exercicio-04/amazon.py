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

print("questao_1:\n Houveram {} queimadas".format(questao_1))
print("questao_2:\n Houveram {} queimadas".format(questao_2))
print("questao_3:\n Houveram {} queimadas".format(questao_3))
print("questao_4:\n Houveram {} queimadas".format(questao_4))