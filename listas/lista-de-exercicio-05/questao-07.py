cont = 0
soma = 0
def valor_pagamento(valor,dias):
	if dias == 0:
		print(valor)

	elif dias>0:
		v=valor+(valor*0.3)+(0.001*dias)
		return v
		
		
while True:
	prestacao = float(input("prestacao: "))
	cont +=1
	if prestacao == 0:
		break
	dias = int(input("dias: "))

	x = valor_pagamento(prestacao, dias)

	print('valor a ser pago: {:.2f}'.format(x))
	soma+=x

print('relatorio: {} prestacoes, soma: {:.2f} '.format(cont-1,soma))
