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
