import random
def jogar():
    def imprime_mesagem_inicial():
        print("#####################################################")
        print("################### JOGO DA FORCA ###################")
        print("############## Frutas/Legumes/Verduras ##############")

    chances = int(input("Selecione a dificuldade (1 - Fácil, 2 - Médio, 3- Difícil"))
    if chances == 1:
        vidas = 15
    elif chances == 2:
        vidas = 10
    elif chances == 3:
        vidas = 5

    acertou = False
    enforcou = False

    arquivo = open('palavras.txt', 'r')
    acervo_palavras = []
    for linha in arquivo:
        linha = linha.strip()
        acervo_palavras.append(linha)
    arquivo.close()
    print(acervo_palavras)
    palavra_secreta = acervo_palavras[random.randint(0, len(acervo_palavras))]

    cabeca = "O"
    braco_esquerdo = "/"
    braco_direito = "\ "
    corpo = "|"
    perna_esquerda = "/"
    perna_direita = "\ "

    letras_acertadas = ['_' for i in range(len(palavra_secreta))]
    while(not acertou and not enforcou):
        print("______________")
        print("|            |")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
        print(letras_acertadas)
        chute = input('Qual a letra?')
        posicao = 0
        for letra in palavra_secreta:
            verifica = len(palavra_secreta)
            if chute.upper() == letra.upper():
                print("Encontrei a letra {} na posição {}".format(letra.upper(), posicao))
                letras_acertadas[posicao] = letra.upper()
            posicao = posicao + 1


        if letras_acertadas == list(palavra_secreta.upper()):
            print("Parabéns você acertou!!!")
            print("Palavra: {}".format(palavra_secreta))
            acertou = True
        elif vidas < 0:
            print("______________")
            print("|            |")
            print("|            {}".format(cabeca))
            print("|           {}{}{}".format(braco_esquerdo, corpo, braco_direito))
            print("|           {} {}".format(perna_esquerda, perna_direita))
            print("|                 ")