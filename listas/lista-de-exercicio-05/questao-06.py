def conversao (horas,minutos):
	if horas>=12:
		v = horas-12
		return v 
	elif horas <=11:
		v1= horas
		return v1

horas=int(input())
minutos=int(input())

recebe = conversao(horas,minutos)
print(recebe)

def periodo (recebe,horas):
	if (horas <=11 ):
		return ("{}:{} A.M".format(horas,minutos))
	else:
		return ("{}:{} P.M".format(horas,minutos))

recebe2 = periodo(recebe,horas)
print(recebe2)
while True:
    continuar=str(input("Deseja continuar? (S/N)"))
    if continuar in "Nao":
        break
    horas=int(input())
    minutos=int(input())
    x=conversao_hora(horas,minutos)
    y=horario(x,minutos)