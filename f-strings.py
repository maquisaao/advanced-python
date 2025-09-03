
nome = "Max Wilson"
altura = 1.77
peso = 80
imc = peso / (altura * altura)
print(nome, 'tem', altura, 'de altura, pesa', peso, 'kgs e seu IMC é', imc)


"f-strings"
# variaveis entre chaves {}
linha_1 = f'{nome} tem {altura:.2f} de altura,' #  usar 2 casas decimais
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
