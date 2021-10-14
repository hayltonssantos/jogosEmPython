import random

def abertura():
    print("***************************")
    print("BEM VINDO AO JOGO DA FORCA")
    print("***************************")

def criaPalavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero].upper()
    return palavraSecreta

def iniciaLetras(palavraSecreta):
   lista = ["_" for letra in palavraSecreta]
   return lista

def chamaChute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def marcaChuteCorreto(chute, palavraSecreta, letrasCertas):
    index = 0
    for letra in palavraSecreta:
        if (chute == letra):
            letrasCertas[index] = letra
        index += 1
    print(letrasCertas)

def imprimeResultado(acertou,enforcou,palavraSecreta):
    if (acertou == True):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    elif(enforcou == True):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavraSecreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    abertura()
    palavraSecreta = criaPalavra()
    letrasCertas = iniciaLetras(palavraSecreta)
    print(letrasCertas)

    enforcou = False
    acertou = False
    erros = 0

  
    while (not enforcou and not acertou):

        chute = chamaChute()


        if (chute in palavraSecreta):
            marcaChuteCorreto(chute, palavraSecreta, letrasCertas)
        else:
            erros +=1
            desenhaForca(erros)

        enforcou = erros == 7
        acertou = "_" not in letrasCertas

    imprimeResultado(acertou,enforcou,palavraSecreta)

if (__name__ == "__main__"):
    jogar()

