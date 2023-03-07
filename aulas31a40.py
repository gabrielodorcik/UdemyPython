#aula31.py

'''
conteudo da aula: id

id = identidade
capacidade de encontrar determinado item na memória

v1 = 'a'
v1 = 'a'
print(id(v1))
print(id(v2))

'''

#aula32.py

'''
conteudo da aula: Flags, is, is not e none

algoritmo são intruções para executar e resolver um problema

com none podemoos usar o is

'''
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print("Não passou no if")

if passou_no_if is not None:
    print("Passou no if")