# atalho para comentar uma linha = crtl + K + C

'''
Isso nao é um comentario, é um docstring (o interpretador do python le o conteudo aqui dentro)
'''


# funcao print:

print(12, 13) # por padrao ele imprime com espaço entre os valores
print(14, 15, sep='-') # parametro "sep" altera o separador entre os valores

print(16, 17) # por padrao imprime com quebra de linha no final (/r/n = CRLF no windows)
print(18, 19, sep='-', end='&') # parametro "end" altera o que vem no final

'''
Python = Linguagem de Programação
Tipo de tipagem = Dinâmica e Forte 
(dinamica = nao precisa declarar o tipo da variavel, ele já sabe o tipo de informação passada)
(forte = nao permite operacoes entre tipos diferentes)

str = string = texto
Strings sao textos que estão dentro de aspas
'''

# escape de caracteres = \
print('Aspas simples: \' ')
print("Aspas duplas: \" ")

# r = raw string = ignora os escapes
print(r"Aspas duplas: \" ")

# escape e raw nao sao muito usados por dificultar a leitura do codigo, solução pra usar aspas:
print('Usar os dois tipos de "aspas" dentro do texto, assim.')
print("O assim: Usar os dois tipos de 'aspas' dentro do texto")



# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.
print(11) # int
print(-11) # int
print(0)

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
print(1.1, 10.11)
print(0.0, -1.5)

# A função type mostra o tipo que o Python
# inferiu ao valor.
print(type('Otávio'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))

# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que
# questiona se um valor é igual a outro

print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))

# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')

''' Variáveis são usadas para salvar algo na memória do computador.
PEP8: inicie variáveis com letras minúsculas, pode usar
números e underline _.
O sinal de = é o operador de atribuição. Ele é usado para
atribuir um valor a um nome (variável).
Uso: nome_variavel = expressão'''

# nome_completo = 'Max Wilson Silva Pinheiro'
# soma_dois_mais_dois = 2 + 2
# int_um = bool('1')
# print(int_um, type(int_um))
# print(nome_completo, soma_dois_mais_dois)

nome = 'Max'
idade = 32
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)