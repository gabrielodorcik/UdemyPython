#aula11.py 
'''
Conteúdo da aula: Procedencia entre os operadores

utilização correta do Parenteses, sempre de dentro para fora
primeiro parentes, depois ** potencialização, depois * / // % e por ultimo subtração e adição

o algoritmo le da esquerda para a direita de baixo para cima, ou seja, sempre em ordem de cascata

'''
# cont_1 = (1 + 1) ** (5 + 5) 
# print(cont_1)

# cont_2 = (1 + int(2.5 - 1.5)) ** (int(10.))
# #mostrando a ordem das coisas
# cont_2 = 1
# print(cont_2)

print("\n")

#aula12.py 

#exercicio de culculo de IMC
#... placeholder, um código que ainda não está terminado, mas que não afeta na funcionalidade do código

# nome = "Gabriel"
# altura = 1.84
# peso = 112.2
# imc = peso / (altura * altura)
 # imc = peso / altura ** 2


print("\n")

#aula13.py

#introdução a f-strings
#reutilizando o ultimo código
#utilizando o f a frente de uma string, a gente pode apenas citar a variavel entre #chaves, assim, não necessita o uso de virgula, e tbm podemos determinar a casa #decimal que vai ser impressa, por exemplo.
#:.2f para limitar as casas decimais

# linha_01 = f'{nome} tem {altura:.2f} de altura'
# linha_02 = f'pesa {peso} quilos e seu imc é '
# linha_03 = f'{imc:.2f}'

# print(linha_01)
# print(linha_02)
# print(linha_03)

# print('\n')

#aula14.py

'''
Conteudo da aula: usando a formatação via format
tudo em python é um objeto

tudo que tem uma ordem começa em 00

podemos nomear uma variavel dentro da função, porem quando precisar ser chamada, necssita desse novo nome para concluir

nome3 = parametro
tudo que vem depois de um parametro nomeado, necessita ser nomeado

'''
# a = 'A'
# b = 'B'
# c = 1.132
# string = 'a={nome1} b={nome2}  b ={nome1} c={nome3:.2f}' #podemos chamar um parametro nomeado dentro de um outro pedido de variavel
# formato = string.format(nome1=a, nome2=b, nome3=c) #argumento nomeado, dando um nome na criação das funções
# print(formato)

#aula15.py

'''
Conteudo da aula: função input

função que é capaz de ler e armazenar um dado pelo usuário

'''
#nome = input('Qual o seu nome? ')
# numero_1 = input("Digite um numero: ")
# numero_2 = input("Digite um outro numero: ")

#fazendo a conversão de tipo
# int_numero_1 = int(numero_1)
# int_numero_2 = int(numero_2)

# print(f'A soma dos numero é {int_numero_1 + int_numero_2}')
#Este método deixa o código mais longo, porém, impede de possiveis quebras de código no futuro
#print(f'o seu nome é {nome}')

#aula16.py

'''
Conteudo da aula : Condicionais

operações condicionais para limitar a sequencia de nosso código
if = se, se um condição for verdadeira, toda condição necessita terminar com :, o if não obrigatoriamente necessita do elif ou else.

elif = é a próxima condição a ser seguida, caso a primiera não seja verdadeira, tbm termina com :, depende do if e do else para funcionar, pode ter um ou mais elif dentro de um bloco de if

else = é o final do if, caso nenhuma outra condição seja verdadeira, ele sera executado, tbm termina com :, depende do if para funcionar

executa tudo que estiver dentro do blocde uma condição
'''
# entrada = input('Você quer "entrar" ou "sair" \n')

# if entrada == 'entrar':
#   print("Você entrou no sistema ")
# elif entrada == 'sair':
#   print("Você saiu do código")
# else:
#   print("Você não digitou nem entrar nem sair")


#aula17.py 
'''
Continuação de condicionais

o código vai checar todas as condições até encontrar a verdadeira, caso não encontrar ele vai executar o else., depois que ele encontrar a verdadeira, ele vai executar e sair do bloco if.

'''
condicao = True
condicao2 = False

# if condicao:
#   print('este é o codigo do if')

# else:
#   print('else do if')

# if 10 == 10:
#   print('verdade')

  
# print('fora do if')

#aula18.py

#falou sobre a ferramenta de debug
# ajuda na hora de entender o código, e analisar o seu desenvolvimneto parte a parte

#aula19.py

'''
Conteudo da aula: operadores de comparação
utilizada para fazer comparação, dentro de condicionais para retornar True ou False
ou dentro de um print tbm

no VSCode: no terminal, usar ls para achar o arquivo com o modolo, após 
python -i aula19.py 
ele vai entrar neste aqquivo em questão e carregar as variaveis

'''
# #um numero maior que outro
# maior = 2 > 1 #true 
# #numero menor que outro
# menor = 6 < 10 #true
# #numero maior ou igual
# maior_igual = 2 >= 1 #retorna true
# #numero menor ou igual
# menor_igual = 1 <= 2 #retorna true
# #numero ou str igual
# igual = 2 == 2, 'a' == 'A' #dois é igual a dois, mas a é diferente de A, sensitve case
# #diferente numero ou str
# diferente = 1 != 2, "a" != "a" #um é diferente de 2 e a ão é diferente de a

#aula20.py
#exercicio de menor e maior, imprimir primeiro o menor

valor_1 = input("Digite um valor: ")
valor_2 = input("Digite um outro valor: ")

if valor_1 >= valor_2:
  print(f'O primeiro valor {valor_1} é maior ou igual que o segundo valor {valor_2}')
else:
  print(f'O segundo valor {valor_2} é maior que o primeiro valor {valor_1}')