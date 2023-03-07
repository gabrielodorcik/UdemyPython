#aula21.py   
"""
Contúdo da Aula: And
todas as condições do andprecisam ser verdadeiras
se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor 
serão consideradas falsy (não confundir com false)
None = não valor, valor não existe
0 é avaliado como falsy, o corpo de if não será executado
"""
# entrada = input("[E]ntrar  [S]air: ")
# senha_digitada = input('Senha: ')
# senha_certa = 'lacoste'

# if entrada == 'E' and senha_digitada == senha_certa:
#   print("Entrar")

# else:
#   print("Sair")

#print(True and True and False and True )
#print(True and 0 and False and True )

#aula22.py  
"""
Conteudo da aula: not

qualquer condição que seja verdadeira, avalia a expressão inteira como verdadeira

"""

# entrada = input("[E]ntrar  [S]air: ")
# senha_digitada = input('Senha: ')
# senha_certa = 'lacoste'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_certa:
#   print("Entrar")

# else:
#   print("Sair")

#print(0 or False or 0 or 'abc' or True)
#ele vai imprimir a primeira condição verdadeira que ele encontrar nesse caso  
#avaliação de curto circuito
#senha = input('Senha: ') or 'sem senha'
#print(senha)

#aula23.py

'''
Conteudo da aula: Not

operador lógico, usado para inverter expressões
not True = False
not False = True

'''

#print(not True) = False
#print(not False) = True

#senha = input("Senha: ")

#if not senha:
    #print("Senha inocrreta.")

#expressão usada para quando nada for inserido no input

#aula24.py

'''
conteudo da aula: in e not in

entre e não está entre
str são interáveis
interavel = item  por item 
0 - 1 - 2 - 3 - 4 - 5 - 6 = indice positivo
g - a - b - r - i - e - l
-7  -6  -5  -4  -3  -2  -1 = indice negativo

'''
#nome = 'Gabriel'
# print(nome[2])
# print(nome[-4])
# print('i' in nome)
# print('f' in nome)
# print(10 * '-')
# print('iel' not in nome)
# print('zero' not in nome)

# usuario = input('Digite uma palavra: ')
# encontrar = input("Digite o que quer encontrar: ")

# if encontrar in usuario:
#     print(f"{encontrar} tem em {usuario}")

# else:
#     print(f'{encontrar} não tem em {usuario}')

#aula25.py

'''
conteudo da aula: interpolação de string com %

mesmo que format porem diferente, tipos são importantes, 
mesmo que o c faz
usamops o % mais uma letra, quando termina a expressão, colocamos um % e depois citamos as variaveis, caso mais que uma, necessita de parenteses
%d ou %i - inteiros
%s = string
%f = float
%x ou &X = exadecimal

nome = 'Gabriel'
preco = 2023.328973
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O haxadecimal de %d é %04X' % (1500, 1500))

'''
#aula26.py

'''
conteudo da aula: Formatação básica de strings
s - string
d - int
f - float
<numeros de digidtos>f
x ou X - hexa
(caractere) (><^) (quantidade)
> esquerda
< direita
^ centro
= ele força o número a aparecer antes dos zeros
sinal - ou +
ex: 0>-100, .f
conversion flags !r = reper, !s = str,  !a = ascii

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{2783.928293781:0=+10,.2f}')
print(f'O haxadecimal de 1500 é {1500:04X}')
print(f'{variavel!r}')


'''
#aula27.py

'''
conteudo da aula: Fatiamento de strings e a função len

as strings são interáveis, podemos acessar item por item via indices, positivo comceça por 0 e negativo começa pelo ultimo indice negativo
0   1  2  3  4  5  6  7  8
O   l  á     m  u  n  d  o
-9 -8 -7 -6 -5 -4 -3 -2 -1

fatiamento [i : f : p ] [::]
i = inicio, vai retornar todos os indices até o final
f = fim, vai me retornar o indice solicitado menos um indice (Ex, pedi o 8 ele termina no 7)
p = passo, de quantos em quantos ele vai pular, geralmnte de 1 em 1

a função len retorna a quantidade, checar tamanho de string
contagem é diferente de indice

variavel = 'Olá mundo'
print(variavel[::])
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[-1:-10:-1]) # string invertida
print(variavel[::-1])# string invertida

'''
#aula28.py
#exercicio com fatiamento, interpolação etc
"""
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print("Seu nome não contém espaços")
    print(f'Seu nome tem {len(nome)} letras')    
    print(f'A primeira letra do seu nome é {nome[0:1:]}')
    print(f'A ultima letra do seu nome é {nome[6:7:]}') #podia usar o indice -1 direto
else:
    print('Desculpe, você deixou campos vazios')

"""
#aula29.py

'''
conteudo da aula:  introdução ao try e except, exceptions

try = tenatr executar o código
except = ococrreu algum erro ao executar

string com sinal de multiplicação é repetição
necessitamos passar o dado do usuário para um int ou float, porque um input sempre vai ser str

isdigit = checa se o usuário usa apenas digitos

numero_str = input(
    'Vou dobrar o número que você digitar: '
)

try: 
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2})
except:
    print('Isso não é um número')

'''

#aula30.py

'''
conteudo da aula: variaveis, constantes, complexidade de código

Constante = variaveis que não vão mudar
muitas condições no mesmo if (ruim)
contagem de complexidade

constante sempre é declarada com letras maiusculas para sua facil identificação

\ é usada para quebrar linha e conytinuar a dar a expressão da conidição
'''



velocidade = 61 # velocidade atual do carro
local_carro = 101 # local do carro na estrada

RADAR_1 = 60 # velocidade máxima do radar
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distancia onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE) 

if velocidade_carro_passou_radar_1:
    print("Velocidade carro passou do radar 1")

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_passou_radar_1:
    print("Carro multado em radar 1")