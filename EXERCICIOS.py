
valorA = float(input("Insira um número inteiro entre 1 - 20: "))
valorB = float(input("Insira um número inteiro-entre 1 - 20: "))
soma = (valorA) + int(valorB)
media = (soma) / 2
print(media)
set = (media) >20
a = 1
b = 20
print("A") if a > b 
--------------------------------------------------------------------------------
#EX0.1
"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade = input("Insira a sua idade: ");
nome = input("Insira o seu nome: ");
print(f"O meu nome é {nome} e tenho {idade} anos. ");
--------------------------------------------------------------------------------
#EX0.2
"""
EX0.2: Output
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("Olá Mundo!");
fruta = "bananas";
print  (f"Eu gosto de {fruta}.");
--------------------------------------------------------------------------------
#EX0.3
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome = input(" Insira o seu nome: ")
print("Olá, {nome} espero que estejas bem: !")
valor = int(input("Insira um número: "))
dobro = valor * 2
print(f"O dobro de {valor} é {dobro}")
--------------------------------------------------------------------------------
#EX1.1
"Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco"

print("\nBem-vindos ao Python!")
--------------------------------------------------------------------------------
#EX1.2
"Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco"

print("\nJosé, bem-vindo ao Python!")
--------------------------------------------------------------------------------
#EX1.3 
"Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável."

mensagem="""
 _   _      _ _        __        __         _     _ _ 
| | | | ___| | | ___   \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)"""
--------------------------------------------------------------------------------
#EX1.4
"Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis."
nome = input ( "Qual o teu nome: ")
idade = int (input ("Qual a sua idade: "))
residencia = input ("Onde você mora: ")
print (f"O nome do aluno é {nome}, a idade do aluno é {idade}, e o aluno mora em {residencia}.")
--------------------------------------------------------------------------------
#EX1.5
"Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem"
--------------------------------------------------------------------------------
linguagemProg = "Python"
nome = "FFF"
print(f"O {nome} sabe programarem no {linguagemProg}")
--------------------------------------------------------------------------------
#EX1.6
"Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres."

print(f"{'Bem-vindo ao Python' : <50}")
print(f"{'Bem-vindo ao Python' : ^50}")
print(f"{'Bem-vindo ao Python' : >50}")
--------------------------------------------------------------------------------
#EX1.7
"Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio."

raio= float(input("Insira o valor do raio: " )) 
perimentro = 2 * 3.14 * raio
area = 3.14 * raio * raio
print(" o valor do perimetro é, {perimetro} , do {raio}" ) 
--------------------------------------------------------------------------------
#EX1.8 
"Elabora um programa que imprima a data e horas correntes nos seguintes formatos"
"02-10-2024"
"02-10-2024 16:11:20"
"10-02-2024 16:11:20"
"02/10/24" 
"16:11:20"

import datetime

x = datetime.datetime.now()
dia = x.strftime("%d")
mes = x.strftime("%m")
ano = x.strftime("%y")
hora = x.strftime("%h")
minutos = x.strftime("%m")
segundos = x.strftime("%s")
print(f"{dia}-{mes}-{ano}")
print(f"{dia}-{mes}-{ano} {hora}-{minutos}")
print(f"{mes}-{dia}-{ano} {hora}-{minutos}")
print(f"{mes}-{dia}-{ano}")
--------------------------------------------------------------------------------
#EX1.9
"Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos."
--------------------------------------------------------------------------------

atleta = input("Digite o número do atleta:")
pontos = input("Digite a pontuação final:")
print(f"O atleta número {atleta} obteve {pontos} pontos.")
--------------------------------------------------------------------------------
#EX.1.10 
"Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual."
dianasc = int(input("Insira a sua data de nascimento:"))
mesnasc = int(input("Insira o seu mes de nascimento:"))
anonasc = int(input("Insira o ano de nascimento:"))
idade = 2024 - anonasc
print(f"Na data atual você tem {idade}:")
--------------------------------------------------------------------------------
#EX1.11
"Elabora um programa que desenvolva o algoritmo de um programa que permita converter libras em euros, considerando a taxa de conversão de 1,19 ( ou seja, 1 GBP = 1,19 EURO)."

libras = int(input("Insira a quantidade de libras:"))
euros =
--------------------------------------------------------------------------------------------------------------------

import random

segredo = int(random.randint (0,5))
#print(f"o número secreto é: {segredo}")

numeroescolhido = int(input("Insira um valor entre (0, 5):"))

if numeroescolhido > segredo:
  print("O número inserido é maior do que eu!")
elif numeroescolhido < segredo:
  print("O número inserido é menor do que o meu!")
else:
  print("\n Acertaste!")

--------------------------------------------------------------------------------------------------------------------
velocidade = int(input("Insira a velocidade em que estava: ")
multa = (velocidade) - 80
valor = (multa) * 7
if velocidade > 80:
  print (f"Excedeste a velocidade em {multa}km/h e vais ter de pagar {valor} $")
else:
  print("Esctavas na velocidade correta!")
--------------------------------------------------------------------------------------------------------------------

num = int(input("Insira o seu numero"))
if num > 0: 
  print("Seu numero é positivo")

elif num < 0:
  print("Seu numero é negativo")

elif num == 0:
 print("Seu numero é zero")


num = int(input("Insira aqui o seu numero "))
if num > 
 print("O seu numero é par")

elif num < 3
 print("o seu numero é impar")

elif num == 0:
 print("O seu numero é zero")
--------------------------------------------------------------------------------------------------------------------

num = int(input("Insira o seu numero"))

nota = int(input("Insira aqui a sua nota:"))
if nota < 10:
 print("Reprovado")
elif nota == 10 and 14:
 print("Suficiente")
elif nota > 15 and nota > 17:
 print("Bom")
elif nota >= 17:
 print("Muito Bom")


  celsius = float(input("Insira a temperatura desejada:"))

  Fahrenheit = celsius * 9/5 + 32
  Kelvin = celsius + 273.15
  input(f"A temperatura em Fahrenheit é {Fahrenheit}")
  if 
  int(f"A teperatura em kelvin é ")

--------------------------------------------------------------------------------------------------------------------

celsius = float(input("Insira a temperatura desejada:"))

Fahrenheit = celsius * 9/5 + 32
Kelvin = celsius + 273.15
input(f"A temperatura em Fahrenheit é {Fahrenheit}")

int(f"A teperatura em fahrenheit é {Fahrenheit}")
print(f" a temperatura em kelvin é {Kelvin}")

--------------------------------------------------------------------------------------------------------------------

salario  = float(input("Insira o valor do salario;:"))
if salario < 1000:
 print("Insira os Impostos")
elif salario >= 1001 and salario <= 2000:
   print("10% do Impostos")
elif salario > 2000:
  print("20% de Impostos")


salario  = float(input("Insira o valor do salario:"))
if salario < 1000:
 print("o seu imposto é zeero está inseto de imposto")
elif salario >= 1000 and salario <= 2000:
 imposto = salario  * 0.10
salarioImposto = salario - imposto 
print(f"O seu salário mensal com o imposto de 10%  é de")
{salarioImposto}
elif salario >= 2000 and :
imposto = salario * 0.20

print("O seu salário mensazl com o imposto de 20% é de:") 
{salarioImposto}
--------------------------------------------------------------------------------------------------------------------
##Exercício FP6: Imprimir números de 1 a 10.
""""Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10."""

for x in range(1,10): 

 print(x)
--------------------------------------------------------------------------------------------------------------------
#Exercício FP7: Soma de números de 1 a 100.
"""Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.
"""

soma = 0
num = 1
while num <= 100:
  soma += num
  num += 1
print(F"A soma de todos os numeros de 1 a 100 é: {soma}")
--------------------------------------------------------------------------------------------------------------------
#Exercício FP8: Contagem de vogais numa string.


frase = input("Escreve uma frase")
vogal = 0
for letra in frase:
  if letra.lower() in "aeiou":
    vogal += 1 
print(f"Esta frase que escreveu tem {vogal} vogais") 
--------------------------------------------------------------------------------------------------------------------
#Exercício FP9: Listar múltiplos de 5.
""""Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50."""

num =  5 
while num <= 50:
  print(num)
  num += 5
---------------------------------------------------------------------------------------------------------------------
"""Exercício FP10: Verificar se um número é primo.
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números."""

num = int(input("Insira o número:"))
if num / 1:
  print("É um número primo")
else :
  print("Não é um numero primo")
---------------------------------------------------------------------------------------------------------------------
#Exercício FP10: Verificar se um número é primo.
"Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números."
1
notas=[]
for i in range (1,4):

  num = int(input("escreva um numero inteiro :"))
  notas.append(num)
printU(notas)
 valor1 = notas[0]
 valor2 = notas[1]
 valor3 = notas[2] 
 valor4 = notas[3]
 valor5 = notas[4]
total= (valor1 + valor2 + valor3 + valor4 + valor5) /5
print(f"a média é":{total}")

2
notas = []
for i in range (0,5) :
    numeros = int(input("Insira um valor inteiro:"))
    notas.append(numeros)
soma = sum(notas)
x = len(notas)
media = (soma / x)
print(media)
---------------------------------------------------------------------------------------------------------------------

"""Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número."""

num = int(input("Insira um numero inteiro"))
div = 0 
for i in range(1, num + 1):   
  if num % i == 0:
   div += 1 
  if div == 2: 
    print(f"o {num} é um numero primo")
  else: 
    print(f"o {num} não é um numero primo ")
  ---------------------------------------------------------------------------------------------------------------------

#FP12
"""Gerar uma lista de números pares.
Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista."""

texto = str(input("Insira um texto "))
textoinv = texto [::-1]
print (textoinv)
 ---------------------------------------------------------------------------------------------------------------------

#""Exercício FP14: Tabuada de multiplicação
""""Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10."""

num = int(input("Insira um numero que quer calcular a tabuada do mesmo:"))
tabuada = []
for i in range(1,11):
  mult = num + i
  print(f"{num} x {i} = {mult}")
-----------------------------------------------------------------------------------------------------------------------

