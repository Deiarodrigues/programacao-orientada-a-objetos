n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))
n3 = int(input("numero 3: "))
if n1>n2 and n1>n3 and n2>n3:
	print("ordem",n1,n2,n3)
elif n1>n2 and n1>n3 and n3>n2:
	print(n1,n3,n2)
elif n2>n3 and n2>n1 and n1>n3:
	print(n2,n1,n3)
elif n2>n3 and n2>n1 and n3>n1:
	print(n2,n3,n1)
elif n3>n1 and n3>n2 and n2>n1:
	print(n3,n1,n2)
elif n3>n1 and n3>n2 and n1>n2:
	print(n3,n2,n1)