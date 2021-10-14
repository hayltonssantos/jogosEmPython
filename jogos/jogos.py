import advinhacao
import forca
import snake

def escolheJogo():
    print("***************************")
    print("ESCOLHA O SEU JOGO")
    print("***************************")

    print("(1) Advinhação || (2) Forca || (3) Snake")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogo de Advinhação")
        advinhacao.jogar()
    elif (jogo == 2):
        print("Jogo da Forca")
        forca.jogar()
    elif (jogo == 3):
        snake.inicia()

if (__name__ == "__main__"):
    escolheJogo()