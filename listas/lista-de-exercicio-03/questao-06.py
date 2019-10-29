x = int(input("Digite um numero: "))
y = int(input("Digite um numero: "))
z = int(input("Digite um numero: "))
if x > y and x > z:
	print("O numero {} e maior que o numero {} e o numero  {}".format(x,y,z))
if y > x and y > z:
	 print("O numero {} e maior que o numero {} e o numero  {}".format(y,x,z))
if z > x and z > y:
	print("O numero {} e maior que o numero {} e o numero  {}".format(z,x,y))