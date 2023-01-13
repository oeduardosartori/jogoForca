def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    palavra_secreta = linha.upper()
    letras_corretas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(f"A palavra possui: {letras_corretas}")

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_corretas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou!\n Você ainda possui {6 - erros} tentaticas.")

        enforcou = erros == 6
        acertou = "_" not in letras_corretas
        print(letras_corretas)

    if (acertou):
        print(f"Parabéns, você acertou a palavra secreta {palavra_secreta}!")
    else:
        print("Que pena, suas chances terminaram e você não conseguiu acertar a palavra secreta")
        print(f"A palavra secreta era {palavra_secreta}")
        print("-------------------- \n Fim do jogo!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
