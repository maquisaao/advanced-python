frase = 'Python é uma linguagem de programação interpretada, de alto nível, orientada a objetos, de código aberto e com sintaxe simples, ideal para iniciantes e profissionais. Ela é usada para desenvolvimento web, ciência de dados, inteligência artificial, automação e projetos científicos, suportando múltiplos paradigmas de programação e possuindo vasta compatibilidade com sistemas operacionais'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)