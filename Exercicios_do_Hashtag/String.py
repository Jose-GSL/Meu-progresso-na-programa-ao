'''Exercício 1: Relatório de Margem de Lucro (Setor Financeiro) Uma empresa de varejo
precisa de um resumo rápido sobre a performance de um produto. Dado o faturamento de
R$ 45.000,00 e o custo de R$ 23.500,00, crie um programa que calcule o lucro e a margem
de lucro (lucro dividido pelo faturamento). Exiba uma mensagem formatada onde o lucro
use o separador de milhar e duas casas decimais, e a margem seja exibida como uma
porcentagem inteira.'''
print('EXERCICIO 1')
faturamento = 45000
custo = 23500

lucro = faturamento - custo
margem = lucro // faturamento

print(f'O lucro foi de R${lucro:,.2f}')
print(f'E a margem foi de {margem:.0%}')

'''Exercício 2: Padronização de Dados de CRM (Setor de Vendas) Um vendedor cadastrou
um cliente com os dados desorganizados no sistema: nome = " mArCoS aNtOnIo
rOcHa " e email = " MARCOS.ROCHA@GMAIL.COM ". Para evitar duplicidade e erros
de envio, você deve:
1. Remover os espaços extras no início e fim das duas variáveis.
2. Deixar o nome apenas com as primeiras letras de cada palavra em maiúsculo
(formato de nome próprio).
3. Deixar o e-mail todo em letras minúsculas. Exiba os resultados finais no console.'''
print('EXERCICIO 2')
nome = "mArCoS aNtOnIo rOcHa"
email ='  MARCOS.ROCHA@GMAIL.COM'
nome = nome.strip().title()
print(nome)

email = email.strip()
email = email.lower()
print(email)

'''Exercício 3: Migração de Servidor de E-mail (Setor de TI) Sua empresa mudou de nome
e todos os funcionários que usavam o domínio @empresa.com.br agora devem usar o
domínio @grupocorp.com. O e-mail do funcionário é andre_silva@empresa.com.br.
Crie um código que substitua automaticamente o domínio antigo pelo novo e exiba o novo
endereço de e-mail.'''
print('EXERCICIO 3')

email_2 = 'andre_silva@empresa.com.br'
novo_dominio = '@grupocorp.com'

#posicao = email_2.find('@')
#print(posicao)
#email_2 = email_2[posicao] + novo_dominio
email_2 = email_2.replace('@empresa.com.br', '@grupocorp.com')

print(email_2)

'''Exercício 4: Extração de Username para Log (Setor de Segurança) Para criar um log de
acessos, o sistema precisa extrair apenas a parte do nome do usuário de um e-mail
corporativo (tudo o que vem antes do @). Dado o e-mail
beatriz.oliveira@grupocorp.com, use a função .find() e o fatiamento de texto
para extrair e exibir apenas o nome beatriz.oliveira.'''

print('EXERCICIO 4')
email_3 = 'beatriz.oliveira@grupocorp.com'
posiçao = email_3.find('@')
username = email_3[:posiçao]
print(username)

'''Exercício 5: Personalização de E-mail de Marketing (Setor de Marketing) O marketing
quer enviar um e-mail de boas-vindas. O cliente forneceu o nome completo: lucas
ferreira souza. Você deve extrair apenas o primeiro nome para usar na saudação (ex:
"Olá, Lucas!"). O código deve:
1. Encontrar a posição do primeiro espaço.
2. Fatiar o texto para pegar apenas o primeiro nome.
3. Formatar o nome com a primeira letra maiúscula.
4. Exibir a mensagem: "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"'''
print('EXERCICIO 5')
mensagem = "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"
nome_2 = "lucas ferreira souza"
posicao_espaco = nome_2.find(" ")
pri_nome = nome_2[:posicao_espaco].capitalize()

mensagem = mensagem.replace("[Primeiro Nome]", pri_nome)
print(mensagem)