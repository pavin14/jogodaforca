import unicodedata
from random import randint



def removedor_de_acentos(palavra: str) -> str:
    normalized = unicodedata.normalize('NFD', palavra)
    return normalized.encode('ascii', 'ignore').decode('utf8')


def forca(letras, crip, partes_boneco, palavra):


    forca = [' ══╦══════╦═              ',
             '   ║     |_|      letras: ',
             '   ║                      ',
             '   ║                      ',
             '   ║                      ',
             '   ║                      ',
             '   ║                      ',
             '═══╩═══════               ']

    morte = 0
    # coloca as partes do boneco na forca
    for a in range(0, 7):
        if partes_boneco[a] == 'x':
            if partes_boneco[6] == 'x': morte = 1
            if a == 0:
                forca[2] = forca[2][:10] + 'O ' + forca[2][12:]
            if a == 1:
                forca[3 + morte] = forca[3 + morte][:9] + '/ ' + forca[3 + morte][10:]
            if a == 2:
                forca[3 + morte] = forca[3 + morte][:10] + '| ' + forca[3 + morte][11:]
                forca[4 + morte] = forca[4 + morte][:10] + '| ' + forca[4 + morte][11:]
            if a == 3:
                forca[3 + morte] = forca[3 + morte][:11] + '\  ' + forca[3 + morte][12:]
            if a == 4:
                forca[5 + morte] = forca[5 + morte][:8] + '_/ ' + forca[5 + morte][10:]
            if a == 5:
                forca[5 + morte] = forca[5 + morte][:11] + '\_ ' + forca[5 + morte][13:]
            if a == 6:
                forca[3] = forca[3][:8] + '-----' + forca[3][12:]
    #printa letra com fundo verde/vermelho
    for d in range(0, 8):
        for e in range(0, 26):
            print(forca[d][e], end='')

            if d == 1 and e == 25:
                for b in range(0, len(letras)):
                    if letras[b] == '@':
                        print(f"\033[0;30;42m{letras[b + 1]}\033[;;m", end=' ')
                    elif letras[b] == '#':
                        print(f"\033[0;30;41m{letras[b + 1]}\033[;;m", end=' ')

            if d == 6 and e == 18:
                for c in range(0, len(crip)):
                    if crip[c] != "*":
                        print(palavra[c], end=' ')
                    else:
                        print('_ ', end='')
        print('')
    print('tentativas restantes:',(partes_boneco.count('x')-7)*-1)



texto = open('palavras.txt', 'r', encoding="utf8")
lista = (texto.readlines())
texto.close()

print('---------Bem Vindo ao jogo da forca!!!!!---------\n'
      '  ═╦═════╦═   \n'
      '   ║    |_|   \n'
      '   ║          \n'
      '   ║          \n'
      '   ║          \n'
      '   ║          \n'
      '   ║          \n'
      '═══╩═══════')  # forca
palavra = (lista[randint(0, len(lista) - 1)]).upper().strip()

crip = list('*' * (len(palavra)))
print('A palavra possui', (len(palavra) - palavra.count('-')), 'letras')
for c in range(0, len(palavra)):
    if palavra[c].isalpha() == 1:
        print('_ ', end='')
    else:
        print('- ', end='')
print('\n')


letra = input(str("Digite uma letra para começar:")).upper()
if (letra == 'Ç') and ('Ç' in palavra):
    letra = 'C'

palavra_mod = removedor_de_acentos(palavra)

contador = 0
partes_boneco = ['V', 'V', 'V', 'V', 'V', 'V', 'V']  # morto = 'XXXXXX'
letras_chutadas = ''
boneco = 0

while True:
    #forca(letra, crip, partes_boneco, palavra)
    if letra == palavra_mod:
        contador = 99
        break

    elif not letra.isalpha():
        forca(letra, crip, partes_boneco, palavra)
        print('Numeros e simbolos nao sao aceitos')

    elif len(letra) != 1:
        forca(letra, crip, partes_boneco, palavra)
        print("somente UMA letra")

    else:
        if letra in letras_chutadas:
            forca(letra, crip, partes_boneco, palavra)
            print('Esta letra ja foi escolhida')

        elif letra in palavra_mod:

            print('voce acertou uma letra')
            contador = 0
            for x in range(0, len(palavra)):

                if letra == palavra_mod[x]:
                    crip[x] = palavra[x]
                    if not letra in letras_chutadas:
                        letras_chutadas = letras_chutadas + (' @' + letra)
                if palavra.find('-') != -1:
                    crip[palavra.find('-')] = '-'

                if crip[x] == palavra[x]:
                    contador = contador + 1
                    if contador == len(palavra):
                        contador = 99

        else:
            print('chute errado')
            letras_chutadas = letras_chutadas + (' #' + letra)
            boneco += 1

            if partes_boneco.count('x') <= 6:
                while True:
                    res = randint(0, 5)
                    if partes_boneco.count('x') == 6:
                        partes_boneco[6] = 'x'
                        break

                    if partes_boneco[res] == 'V':
                        partes_boneco[res] = 'x'

                        break
    forca(letras_chutadas, crip, partes_boneco, palavra)
    if boneco < 7 and contador != 99:
        letra = input(str("Outra letra:")).upper()

        if ((letra == 'Ç') and ('Ç' in palavra)) or (('C' in letra) and ('Ç' in palavra)):
            if 1 >= len(letra):
                letra = 'C'

    if letra == palavra_mod or letra == palavra:
        contador = 99
        forca(letras_chutadas, crip, partes_boneco, palavra)
        break

    elif (boneco >= 7) or (contador == 99):
        forca(letras_chutadas, crip, partes_boneco, palavra)
        break

        # se o contador estiver em 99 a palavra esta certa
        # se o c for maior que 6 voce perde
        # variaveis para usar em forca: contador, erro, crip ,boneco, palavra
        # em erro % representa letras erradas e & letras certas

if contador == 99:
    print('PARABENS, voce acertou a palavra e salvou o boneco :)')

if contador != 99:
    print('Que pena nao foi dessa vez que :(\n palavra:',palavra)
