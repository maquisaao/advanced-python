'''
Exercicio: fazer um programa pra identificar a letra que mais aparece na frase. usar while e desconsiderar o ' ' (espaço)
'''

frase = 'Python é uma linguagem de programação interpretada, de alto nível, orientada a objetos, de código aberto e com sintaxe simples, ideal para iniciantes e profissionais. Ela é usada para desenvolvimento web, ciência de dados, inteligência artificial, automação e projetos científicos, suportando múltiplos paradigmas de programação e possuindo vasta compatibilidade com sistemas operacionais'


indice = 0 
letra_sendo_usada = []
letra_vencedora = []
letra_atual = []
qnt_vezes_letra_atual_apareceu = 0
qnt_vezes_letra_anterior_apareceu = 0

while indice < len(frase.lower()):

    letra_atual = frase[indice]
    qnt_vezes_letra_atual_apareceu = frase.count(letra_atual)

    if qnt_vezes_letra_atual_apareceu < qnt_vezes_letra_anterior_apareceu:
        letra_vencedora = letra_atual
        indice += 1
    else:
        
        indice +=1

    
    





