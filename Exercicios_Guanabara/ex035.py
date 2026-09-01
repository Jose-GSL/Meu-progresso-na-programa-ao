print('-=-' * 8)
print('Analisandor de triângulos')
print('-=-' * 8)

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if (n1 + n2 > n3) and (n1 + n3 > n2) and (n2 + n3 > n1):
    print('Os segmentos acima PODEM FORMA um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMA um triângulo!')