"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
# condicao = True

# while condicao:
#     nome = input('Qual o seu nome: ')
#     print(f'Seu nome é {nome}')

#     if nome == 'sair':
#         break # sai do bloco

# print('Acabou')

# contador = 0 

# while contador < 10:
#     print(f'{contador}')
#     contador += 1 # mesmo que ( contador = contador + 1 )

# = += -= *= /= //= **= %=

'''
usando continue para 'pular' acoes
'''
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')

'''
while dentro de while
'''

# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1
# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna += 1
#     linha += 1
# print('Acabou')

'''
EXERCICIO: ITERANDO STRINGS COM WHILE
criar alguma mudanca usando while e ltras do nome
'''
#------ como eu resolvi --------
nome = 'Max Wilson Silva Pinheiro'
tamanho_nome = len(nome)
print(f'{nome} tem {tamanho_nome} letras')

indice = 0
nome_novo = ''
while indice < 25:
    letra = nome[indice] + '*'
    nome_novo += letra
    indice += 1
print (nome_novo)

# ------ solucaao do otavio ---
nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)

""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')

