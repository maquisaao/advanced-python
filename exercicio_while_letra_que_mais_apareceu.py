'''
Exercicio: fazer um programa pra identificar a letra que mais aparece na frase. usar while e desconsiderar o ' ' (espaço)
'''

frase = 'Python é uma linguagem de programação interpretada, de alto nível, orientada a objetos, de código aberto e com sintaxe simples, ideal para iniciantes e profissionais. Ela é usada para desenvolvimento web, ciência de dados, inteligência artificial, automação e projetos científicos, suportando múltiplos paradigmas de programação e possuindo vasta compatibilidade com sistemas operacionais'


indice = 0 
qnt_vencedora = 0
letra_vencedora = ''

while indice < len(frase):
    letra_atual = frase[indice]

    if letra_atual == ' ': 
        indice += 1
        continue

    qnt_atual = frase.count(letra_atual)

    if qnt_vencedora < qnt_atual:
        qnt_vencedora = qnt_atual
        letra_vencedora = letra_atual

    indice += 1

print(f'A letra que apareceu mais vezes foi "{letra_vencedora}" que apareceu {qnt_vencedora}x')


    





