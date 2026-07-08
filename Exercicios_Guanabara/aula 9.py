'Modos de como manipular strings em python'
frase = 'Curso em Video Python'

#fatiamento
print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(' ')
#analise 

print(len(frase)) #para saber quantas letras tem 
print(frase.count('o',0,14)) #para contar caracterios 
print(frase.find('deo'))#encoontra a posiçaõ da palavra ou string
print('Curso' in frase)# certifica se tem ou nao na string, mandando true ou false 

#tranformação
print(' ')
print(frase.replace('Python','Adroind'))#substitue uma palavra por outra 
print(frase.upper())#tranforma a string em maiusculo
print(frase.lower())#tranforma a string em minusculo
print(frase.capitalize())# Transforma a primeira letra em maiusculo
print(frase.title())#Vai tranforma a primeira letra em maiculo de cada palavra 
print(frase.strip())#tira os espaços desneceraios, arrumado a string, se colocar r(direita) ou l(esquerda)
#no comeco de strip, vai dirar so desse lado  

#divisão
print(' ')
print(frase.split())#vai dividir a string depois dos espaços e tranformar a string em uma lista 
print('-'.join(frase))#Ele junta a string e coloca o carcatere que vc deseja 











