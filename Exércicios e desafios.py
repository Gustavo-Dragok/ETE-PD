#ETE PORTO DIGITAL
#LPC - introdução a python
#prof. Cloves Rocha
#Aluno : Gustavo Felipe Barros De Souza 1B


# Exercício 1. Faça um Programa que mostre a mensagem "Olá mundo" na tela :

print ('olá mundo ')

# Exercício 2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número] :

numero = int(input('Diga-me um número : '))
print('o número informado foi ',numero)

# Exercício 3. Faça um Programa que peça dois números e imprima a soma :

n1 = int(input('fale-me um número : '))
n2 = int(input('fale-me outro número : '))
print (f'A soma entre {n1} e {n2} resulta em : {n1+n2}')

# Exercício 4  Faça um Programa que peça as 4 notas bimestrais e mostre a média :

n1 = float(input('primeira nota : '))
n2 = float(input('segunda nota : '))
n3 = float(input('terceira nota : '))
n4 = float(input('quarta nota : '))
media = (n1+n2+n3+n4)/4
print (f'sua media é {media}')

# Exercício 5. Faça um Programa que converta metros para centímetros :

metros = float(input ('Metros a ser convertido : '))
cent = metros*100
print (f'{metros}M convertidos para centímetros são {cent}Cm')

# Exercício 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área :

raio = float(input('Raio do círculo : '))
area = (raio**2) * 3.14
print (f'A área do círculo é {area} (m/cm)')

# Exercício 7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário:

lado = float(input('lado do quadrado : '))
area = lado**2
print (f'O dobro da área do quadrado é : {area*2}')

# Exercício 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês:

porhora = float(input ('Quanto você recebe por horas trabalhadas? '))
hora = float(input ('Quantas horas você trabalha pro mês? '))
salario = porhora*hora
print (f'Você recebe R${salario} pelo mês trabalhado')

# Exercício 9 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo: 

valor = int(input ('Digite um valor : '))
if valor < 0 :
    print (f'O valor {valor} é um numero negativo')
elif valor == 0 :
    print (f'o valor {valor} é um número neutro')
else :
    print (f'O valor {valor} é um número Positivo')

# Exercício 10. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido :

sexo = str(input ('Qual o seu sexo ? [F,M] '))
print (' ')
if sexo in "F" :
    print ('Seu sexo é Feminino')
elif sexo in "M" :
       print ('Seu sexo é o Masculino')
else :
    print ('Sexo inválido')

# Exercício 11. Faça um Programa que verifique se uma letra digitada é vogal ou consoante:

letra = str(input('Me fale uma letra : '))
print ('-'*20)
if letra == "aeiou" or "AEIOI":
    print(f'A letra {letra} é uma vogal')
else :
    print (f'A letra {letra} é uma consoante')
