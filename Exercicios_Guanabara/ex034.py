salario = float(input('Digite seu salario atualdo funcionario: R$'))
if salario > 1250:
    salario_atual = salario * 10 / 100 + salario
if salario <= 1250:
    salario_atual = salario * 15 / 100 + salario
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario_atual:.2f} agora.')