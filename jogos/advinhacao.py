def jogar():
    import random
    print("*******************************")
    print("Bem vindo ao jogo de advinhação")
    print("*******************************")

    "Variaveis"
    vezesDeChute = 4
    rodada = 0
    numeroSecreto = random.randrange(1,101)
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Facil || (2) Medio || (3) Dificil")
    nivel = int(input("Escolhe o nivel: "))

    if (nivel == 1):
        vezesDeChute = 20
    if (nivel == 2):
        vezesDeChute = 10
    if (nivel == 3):
        vezesDeChute = 5


    for rodada in range (1, vezesDeChute + 1):  
        print("Tentativa {} de {}".format (rodada,vezesDeChute))
        chute = int(input("Digite um numero entre 1 e 100: "))

        if (chute < 1 ) or (chute > 100):
            print("Chute somente acima ou igual a 1!")
            continue
        "Testes"
        acertou = chute == numeroSecreto
        maior = chute > numeroSecreto
        menor = chute < numeroSecreto
    
        if (acertou):
            print("voce ganhou e fez {}", pontos)
            break
        else:
            if (maior):
                print("Seu chute {} foi menor".format(chute))
            elif (menor):
                print("Seu chute {} foi menor".format(chute))
                pontosPerdidos = abs(numeroSecreto - chute)
                pontos = pontos - pontosPerdidos
    print("Fim de jogo")

if (__name__ == "__main__"):
    jogar()
