peso_de_peixes = float(input("digite o peso: "))
peso = float(50)
if peso_de_peixes > peso:
	excesso = (peso_de_peixes - peso)
	multa = excesso * 4.00
	print("O peso dos peixes foi {:.2f} \n O peso estabelecido pelo regulamento de Sao paulo {:.2f} \n O excesso foi de {} \n A multa foi de {} por quilo de peixe.".format(peso_de_peixes,peso,excesso,multa))