def data(dia,mes,ano):
	meses = [0,"janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

	dia = int(dia)
	mes = int(mes)
	ano = int(ano)

	if mes>=1 and mes <=12:
		print("{} de {} de {}".format(dia,meses[mes],ano))
	elif mes != meses:
		print("NULL")

dia,mes,ano = input().split("/")

x = data(dia,mes,ano)
