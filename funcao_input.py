# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

# numero_1 = input('Digite um número: ') # sempre retorna em tipo str
# numero_2 = input('Digite outro número: ')

# int_numero_1 = int(numero_1) # 
# int_numero_2 = int(numero_2)

# print(f'A soma dos números é: {int_numero_1 + int_numero_2}')

# entendendo o fluxo do interpretador 

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')