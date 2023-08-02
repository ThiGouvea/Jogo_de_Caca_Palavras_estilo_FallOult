import random, palavras


def EscolhendoDificuldade():
    print('QUAL DIFICULDADE DESEJA FACIL/MEDIO/DIFICIL')
    input_correto = True
    while input_correto:
        dificuldade = input('> ')
        if dificuldade.strip().upper() == 'FACIL':
            return 'facil'
            input_correto = False
        elif dificuldade.strip().upper() == 'MEDIO':
            return 'medio'
            input_correto = False
        elif dificuldade.strip().upper() == 'DIFICIL':
            return 'dificil'
            input_correto = False
        else:
            print('SOMENTE FACIL/MEDIO/DIFICIL')

def GerarTela(palavras):
    caracteres_aleatorios = '!@#$%&(")_{}[]/?><,.'
    enderecos_hex = ['0x67A8F2B4', '0x0C6398A7', '0x524E1DFA', '0x9D70C5E2', '0x81B64F03', '0x3F291E8D', '0xE4C17A59', '0x106DABF6', '0x732F8B20', '0x5E9C03D8', '0xF7A205B1', '0xA823E40C', '0x1BDF6795', '0x88C4026F', '0xD69B7FE8', '0x972ED8B3', '0x4FAA6C15', '0x3851B907', '0x56E2CDA6', '0x99A7F1ED', '0x742E8E63', '0xA4FD0921', '0x1C670B3F', '0xC8A593DF', '0x7E4FB2CD', '0xF2E1768D', '0x40C39A50', '0x29DA6FB8', '0x8B9E4322', '0xDE61C9A4', '0x675A83F9']
    for i in range(len(palavras) - 1):
        tamanho_total_caracteres = 0
        print(enderecos_hex[i], '  ', end="")
        for u in range(random.randint(1, 7)):
            numero_aleatorio = random.randint(0, 18)
            print(caracteres_aleatorios[numero_aleatorio], end="")
            tamanho_total_caracteres += 1
        print(palavras[i].upper(), end="")
        for u in range(15 - tamanho_total_caracteres):
            numero_aleatorio = random.randint(0, 17)
            print(caracteres_aleatorios[numero_aleatorio], end="")
        print()

def Input(tamanho_palavra):
    palavra_digitada = input('> ')
    palavra_digitada = palavra_digitada.strip().upper()
    palavra_digitada = palavra_digitada[0:tamanho_palavra]
    return palavra_digitada

def Comparador(palavra, inserido):
    acertos = 0
    for i in range(0, len(palavra)):
        if palavra[i] == inserido[i]:
            acertos += 1
    return acertos


def main():
    dificuldade_jogo = EscolhendoDificuldade()
    palavras_nivel = palavras.GeradorDePalavrasAleatorias(dificuldade_jogo) 
    palavra_aleatoria = palavras_nivel[random.randint(0, len(palavras_nivel) - 1)]
    GerarTela(palavras_nivel)
    print()
    tentativas = 0
    while True:
        inserted = Input(len(palavra_aleatoria))
        print('>', inserted, end=" ")
        acertadas = Comparador(palavra_aleatoria, inserted)
        print(acertadas, "/", len(palavra_aleatoria))
        if acertadas == len(palavra_aleatoria):
            print('SUCESSO')
            break
        else:
            tentativas += 1
            if tentativas == 4:
                print('VOCE PERDEU')
                break

if __name__ == '__main__':
    main()

