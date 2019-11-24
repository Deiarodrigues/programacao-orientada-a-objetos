import random
def embaralhar(x):
	p = list(x)
	random.shuffle(p)
	p = "".join(p)

	p = "".join(random.sample(x, len(x)))
	print(p)

palavra = input("esceva um palavra: ")
x = embaralhar(palavra)
