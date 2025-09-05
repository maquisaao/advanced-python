# receber dois valores, comprarar e mostrar o maior primeiro e o menor depois e com seus valores na tela
# exemplo: O Numero 1 = '2' é maior que o Numero 2 = '1'

numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')

if numero_1 > numero_2:
    print(f'O {numero_1=} é maior que o {numero_2=}')
else:
    print(f'O {numero_2=} é maior que o {numero_1=}')