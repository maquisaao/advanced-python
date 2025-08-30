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