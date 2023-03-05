#aula01.py 
#aulas iniciais falamos sobre comentários, que é feito com o uso de hashtags ou por doctring, como abaixo, aspas simples ou duplas, para mais linhas de códigos
"""
print("hello world")

"""
print(1234,"\n")
print("\n")

#aula02.py
#Nessa aula famlos sobre a função print, Python é uma linguagem Sensitive Case, ou seja, letras maiuculas e minusculas possuem diferença
print(20, 12, sep=" 5 ", end=' #\n')
print(32, 90, sep=' - ', end=" : \n")
#sep = separa os valores da string com o caracter desejado
#end = o final do print
print("\n")

#aula03.py
"""
Conteudo da aula:

Python é uma linguagem de tipagem dinâmica e forte
str = string

"""
print("Python é a melhor linguagem!")
print("\n")

#aula04.py
'''
Aula de hoje: Tipo de dados
numeros inteiros, positivo ou negativos

numeoros floats, numero com casas decimais, divididos com ., positivos e negativos 

função para ver o tipo de dado, na realidade é uma classe, mas falamos função.
type(), usamos para descobrir, int, float, str, boll(bollean), etc
'''
print(12, -70, 0)#int
print(21.9, -92.5, 0.5)#float
print(type(2),type("Hello"), type(10.8))#classe type

print("\n")

#aula05.py

"""
Conteudo da aula: Bollean
Só tem dois valores True(verdadeiro) ou False(falso)
Tipo de dado lógico, muito usado em condicionais
Usamos o operador lógico == ou !=
Igual ou diferente

"""
print(20 == 2, 20 != 5, sep=',') 
print("Hello" == 'hello')
print('Gabriel' == "Gabriel")
print(type("Hello" == 'hello')) #type só me devolve o tipo, mas não a operação

print("\n")

#aula06.py 

"""
Conteudo da aula: Coerção de dados
conversão de tipos, Type Convertion, Typecasting, Coersion
Ato de converter um tipo em outro tipo
Tipos imutaveis e primitivos
Imutaveis = str, int, float, bool
Não podemos concatenar dados d etipos diferentes

Para realizar a conversão, devemos passar o numero através de uma classe desse determinado tipo

As funções são lidas de dentro para fora

"""
# print(1 + 1)
# print("1" + 1)
print(int('1'), type(int('1'))) # a principio o 1, entrou como str, mas foi convertido em um numero inteiro
print(float('2.0') - 1) # podemos realizar operações, juntamente com a conversão
print(bool(''))  # str sem espaço é false, str com espaço é true
print('b' + str('12')) #concatenado um int convertido em str com uma str

print("\n")

#aula07.py 

'''
Conteúdo da aula: Váriaveis
PEP 8, Guia de estilos da linguagem python
Variaiveis = usadas para salvar dados no programa
PEP8 = iniciar vaiáveis com letras minusculas, podendo usar numeros e underlines
= é um operador de atribuição a variavel
Atribuindo um valor a ela

utilização de variaveis, facilita a digitação e agiliza o código

'''
# nome = "Gabriel"
# sobrenome = "Odorcik"
# nome_completo = "Gabriel Odorcik"
# idade = 19
# maior_idade = idade >= 18
# print(nome,sobrenome, sep=" ")
# #utilizando o código da aula passada
# int_um = int('1')
# type_int_um = type(int('1'))
# print(int_um, type_int_um)
# print("Nome:",nome, "Idade:",idade)
# print("É maior de idade? ", maior_idade)

print("\n")

#aula08.py 
'''
Conteudo da aula: exercicio simples usando print

'''
# nome = "Gabriel"
# sobrenome = "Odorcik"
# idade = 19
# ano_nascimento = 2023 - idade
# maior_de_idade = idade >= 18
# altura_metros = 1.84
# print("Nome: ", nome)
# print("Sobrenome: ", sobrenome)
# print("Idade: ", idade)
# print("Ano de nascimento: ", ano_nascimento)
# print("É maior de idade? ", maior_de_idade)
# print("Altura em metros: ", altura_metros)

print('\n')

#aula09.py

# Conteudo da aula: Operadores matemáticos

# + adição
adicao = 1 + 3, 4 + 4.2
print(adicao)
# - subtração
subtracao = 4 - 2, 2 - 0.5
print(subtracao)
# / divisão sempre o retorno é float
divisao = 10 / 2.2
print(divisao)
# * multiplicação
multiplicacao = 2 * 30, 0.5 * 4
print(multiplicacao)
# divisão inteira // todo resultado após o ponto, não vai ser impresso
divisao_inteira = 10 // 2.2
print(divisao_inteira)
#exponenciaçao ** um numero elevado a outro
exponenciacao = 2 ** 4
print(exponenciacao)
# resto da divisão %
modulo = 25 % 5 
print(modulo)
# muito usado para encontrar um numero que é multiplicado por outro
print(10 % 4 == 0)
print(10 % 2 == 0) #descobri se é par

print('\n')

#aula10.py

'''
conteudo da aula: operadores de concatenação e repetição
+ concatenação
dados do mesmo tipo, soma esses valores no print e imprime na ordem desejada

* repetição
repete uma determinada de vezes um valor escolhido

'''
concatenacao = 'A' + 'B' + 'C'
print(concatenacao)

concatenacao_dois = 'P' + 'S' + str('2') 
print(concatenacao_dois)

a_dez_vezes = 'A' * 10
print(a_dez_vezes)

tres_vezes_gab = 'gab,' * 3
print(tres_vezes_gab )