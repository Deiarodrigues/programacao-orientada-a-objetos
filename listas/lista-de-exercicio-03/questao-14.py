nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2)/2
 if media > 0 and media <= 4.0:
print('Media: %.2f, Conceito: E.' % (media))
elif media > 4.0 and media <= 6.0:
 print('Media: %.2f, Conceito: D.' % (media))
elif media > 6.0 and media <= 7.5: 
print('Media: %.2f, Conceito: C.' % (media)) 
elif media > 7.5 and media < 9.0:
 print('Media: %.2f, Conceito: B.' % (media))
elif media > 9.0 and media <= 10.0:
print('Media: %.2f, Conceito: A.' % (media))
else:
print('Nota inválida, Nota1: %.2f, Nota2: %.2f' % (nota_1, nota_2))

