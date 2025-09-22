'''
calculadora com while
receber 2 valores e o operador do usuaio e retornar com resultado e operacao (ex: a soma de x e y é z)
'''

print('Bem vindo a calculadora')
menu = input('Voce quer Entrar(1) ou Sair?(2)\n')

while menu == '1':
    a = int(input('')) #primeiro valor
    op = input('') #operador ( + - * /)
    b = int(input('')) #segundo valor
    
    if op == '+' and menu == '1':
        resultado = a + b
        print(f'A soma de {a} e {b} é {resultado}')
        menu = input('Fazer outra conta?')
    elif op == '-' and menu == '1':
        resultado = a - b
        print(f'A subtracao de {a} e {b} é {resultado}')
        menu = input('Fazer outra conta?')
    elif op == '/' and menu == '1':
        resultado = a / b
        print(f'A divisao de {a} e {b} é {resultado}')
        menu = input('Fazer outra conta?')
    elif op == '*' and menu == '1':
        resultado = a * b
        print(f'A multiplicacao de {a} e {b} é {resultado}')
        menu = input('Fazer outra conta?')

print('Voce saiu da calculadora')

#------- resolucao do professor

""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if op == '+':
        print(num_1_float+num_2_float)
    elif op == '-':
        print(num_1_float-num_2_float)
    elif op == '/' and menu == '1':
        print(num_1_float/num_2_float)
    elif op == '*' and menu == '1':
        print(num_1_float*num_2_float)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break