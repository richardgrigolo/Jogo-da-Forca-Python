import random

print('--------- Jogo da Forca -------------')

letras_acertadas = ''
numero_tentativas = 0

escolha_um = input('Digite "1" para Jogo Solo ou "2" para Jogo em Dupla: ')

while escolha_um not in ['1', '2']:
    escolha_um = input('Opção inválida. Digite "1" para Solo ou "2" para Dupla: ')

if escolha_um == '1':
    palavra_chave = ['chocolate', 'constitucional', 'detergente', 'piscicultura']
    palavra_secreta = random.choice(palavra_chave)

else:
    palavra_secreta = input('Digite a palavra para o oponente adivinhar: ').lower()

print('\n' * 100)

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1 and letra_digitada != palavra_secreta:
        print('Palavra errada.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '_'

    print('Palavra formada:', palavra_formada)

    if numero_tentativas > 5:
        print('VOCÊ PERCEU!')
        print('A palavra era', palavra_secreta)
        break

    if palavra_formada == palavra_secreta or letra_digitada == palavra_secreta:
        print('VOCÊ ACERTOU! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
        break