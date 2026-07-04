dia = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodado? '))
#valor_dia = dia * 60
#valor_km = km * 0.15
#total = valor_dia + valor_km 
total = (dia * 60) + (km * 0.15)
print(f'O total a pagar e de R${total:.2f} reais')