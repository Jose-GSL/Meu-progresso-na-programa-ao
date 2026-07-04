from math import sin, cos, tan, radians
ângulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(ângulo))
coss = cos(radians(ângulo))
tang = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem o seno de {seno:.2f}')
print(f'O ângulo de {ângulo} tem o cosseno de {coss:.2f}')
print(f'O ângulo de {ângulo} tem o tangente de {tang:.2f}')


