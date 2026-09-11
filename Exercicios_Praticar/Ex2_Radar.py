'''Desafio: O Radar da Patrulha Estelar

Você foi contratado pela Patrulha Estelar para criar o sistema de monitoramento 
do setor espacial. O script deve registrar uma nave, validar os dados do piloto 
e verificar a velocidade.

Requisitos do Código:
Entrada de dados:

Solicite o nome do piloto .

Solicite a velocidade da nave (em km/h).

Tratamento de String:

Remova os espaços desnecessários do início e do fim do nome usando .strip().

Verifique se o nome do piloto contém a palavra "Silva"(independente 
de guardas/minúsculas) e exiba essa verificação ( Trueou False).

( mathe random):

Calcule quantas horas a nave levaria para percorrer uma distância introduzida 
de 1.000 km ( tempo = 1000 / velocidade). Use math.ceil()para arredondar esse 
tempo de viagem para o próximo número inteiro acima.

Gere um número de protocolo de autorização aleatória de 4 dígitos (entre 1000e 
9999) usando random.randint().

Condicionais ( if/ else):

O limite de velocidade espacial é 80 km/h .

Se a velocidade for maior que 80 km/h: Calcule e exiba uma multa no valor de 
R$ 7,00 para cada km/h acima do limite .

Se a velocidade for menor ou igual a 80 km/h: Exiba a mensagem "Navegação em 
velocidade segura. Boa viagem!" .'''


import math
import random 

nome = str(input('Nome do piloto: ')).lower().strip()
velocidade = float(input('velocidade da nava: '))
separaçao = nome.split()
tempo = math.ceil(1000 / velocidade)
autorização = random.randint(1000, 9999)

print(f'O piloto tem silva no nome? {'silva' in nome}')
print(f'Tempo estimado para uma viagem de 1000 km? {tempo} hora (s)')

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('[ALERTA] Você ultrapassou o limite de 80 km/h!')
    print(f'MULTA APLICADA: R$ {multa:.2f} (R$ 7.00 por km excedido)')
else:
    print('Navegação em velocidade segura. Boa viagem!')



