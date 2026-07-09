#ver se sua cidade começa com o nome santos.
cidade = str(input('Digite o nome da sua cidade: ')).strip()
separador = cidade.split()
print('Santos' in  separador[0].capitalize())
