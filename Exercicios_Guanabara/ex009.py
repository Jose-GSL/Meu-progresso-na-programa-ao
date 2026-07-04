valor = int(input('Digite um numero para a tabuada:'))
numero = [1,2,3,4,5,6,7,8,9,10]
print('-' * 12)
for item in  numero:
    resultado = valor *  item
    print(f'{valor} x {item} = {resultado}')
 # type: ignore