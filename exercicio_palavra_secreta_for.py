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

palavra_secreta = 'jesus'
letras_acertadas = ''
qnt_letras_digitadas = 0

while True:
    letra_digitada = input('Digite UMA letra:')

# garantir que seja enviada apenas UMA letra por vez e sinalizar o usuario se sair mais (acho que da pra usar continue)
    if len(letra_digitada) > 1:
        print('Digite apenas UMA letra!')
        continue

    if letra_digitada in palavra_secreta: # validar se a letra digitada está na palavra secreta 
        letras_acertadas += letra_digitada # guardar cada letra acertada e concatenar com as letras acertadas)
        
    palavra_digitada = '' # iterar a palavra secreta e se for correta, printar a letra, se nao for printar *
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_digitada += letra_secreta
        else:
            palavra_digitada += '*'
    qnt_letras_digitadas += 1 # implementar as tentativas até finalizar o jogo

    print(f'{palavra_digitada}')

    if palavra_digitada == palavra_secreta: # sinalizar que venceu e quantas tentativas
        print(f'Parabens, voce acertou a palavra secreta que era: {palavra_secreta}.')
        print(f'Voce fez {qnt_letras_digitadas} tentativas.')
        break
