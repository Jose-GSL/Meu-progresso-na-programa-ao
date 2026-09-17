'''Analisando Triângulos v2.0'''

n1 = float(input('PRIMEIRO SEGMENTO: '))
n2 = float(input('SEFUNDO SEGMENTO: '))
n3 = float(input('TERCEIRO SEGMENTO: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima podem forma um triangulo')
    if n1 == n2 == n3:
        print('EQUILATERO')
    if n1 != n2 != n3:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmento acima nao podem forma um triangulo')
