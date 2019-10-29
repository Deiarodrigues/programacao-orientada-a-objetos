p1 = float(input("produto 1: "))
p2 = float(input("Produto 2: "))
p3 = float(input("Produto 3: "))
if p1<p2 and p1<p3:
	print("comprar produto 1 que e: {:.2f}".format(p1))
elif p2<p1 and p2<p3:
	print("comprar o produto 2 que e: {:.2f}".format(p2))
elif p3<p1 and p3<p2:
	print("comprar o produto 3 que e:{:.2f}".format(p3))