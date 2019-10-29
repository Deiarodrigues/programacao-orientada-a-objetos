turno = input("turno(M/V/N): ")
if turno in "m":
	print("Bom dia!")
elif turno in "v":
	print("Boa Tarde!")
elif turno in "n":
	print("Boa Noite")
else:
	print("valor invalido")