def somaimposto(taxa_imposto,custo_do_produto):
    porcentagem = taxa_imposto/100
    custogeral= custo_do_produto+(porcentagem*custo_do_produto)
    return custogeral
taxa_imposto=int(input("porcentagem:"))
custo_do_produto = float(input("custo do produto:"))
print(somaimposto(taxa_imposto,custo_do_produto))

