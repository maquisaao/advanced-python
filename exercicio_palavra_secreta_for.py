"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


# validar se a letra digitada está na palavra secreta 
# guardar cada letra acertada (talvez concatenando com a lista das letras acertadas)

while True:
    letra_digitada = input('Digite UMA letra:')

# garantir que seja enviada apenas UMA letra por vez e sinalizar o usuario se sair mais (acho que da pra usar continue)
    if len(letra_digitada) > 1:
        print('Digite apenas UMA letra!')
        continue

    