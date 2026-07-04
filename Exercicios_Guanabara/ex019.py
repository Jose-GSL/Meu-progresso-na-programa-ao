import random
primeiro = str(input('Primeiro aluno:'))
segundo = str(input('Segundo aluno:'))
terceiro = str(input('Terceiro aluno:'))
quarto = str(input('Quarto aluno:'))

alunos = [primeiro,segundo,terceiro,quarto]
print(f'O aluno escolhido foi {random.choice(alunos)}')