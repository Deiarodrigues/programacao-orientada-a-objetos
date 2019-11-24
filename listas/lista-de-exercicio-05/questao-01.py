def enesima_linha(numero):
    for linha in range(1,numero+1):
        print("{}{}".format(linha," ")*linha)
n = int(input("numero:"))
num=enesima_linha(n)
