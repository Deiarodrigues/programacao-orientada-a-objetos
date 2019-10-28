ganha = float(input("quanto voce ganha por hora no mes? "))
horas = int(input("quantas horas voce trabalha? "))
salario_bruto = (ganha*horas)*30
imposto_de_renda = salario_bruto*(11/100)
inss =  salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto -(imposto_de_renda + inss + sindicato)
print(" O salario bruto e de {:.2f}:\n O imposto de renda e de {:.2f}\n O inss de {:.2f}\n O sindicato de {:.2f}\n Salario liquido de {:.2f}".format(salario_bruto,imposto_de_renda,inss,sindicato,salario_liquido))