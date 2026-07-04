import random 
n1 = str(input('Primeriro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('terceiro aluno:'))
n4 = str(input('Quarto aluno:'))

ordem = [n1,n2,n3,n4]
random.shuffle(ordem)

print('A ordem de aoresentaçao sera de ')
print(ordem)