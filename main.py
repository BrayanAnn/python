import random

print("#####################################################")
print("################### JOGO DA FORCA ###################")
print("############## Frutas/Legumes/Verduras ##############")
acertou = False
enforcou = False
acervo_palavras = [
    'Banana',
    'Tomate',
    'Alface',
    'Repolho',
    'Abacaxi',
    'Uva',
    'Manga',
    'Beringela',
    'Coentro',
    'Cebola',
]

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
    print("|            {}".format(cabeca))
    print("|           {}{}{}".format(braco_esquerdo, corpo, braco_direito))
    print("|           {} {}".format(perna_esquerda, perna_direita))
    print("|                 ")
    print(letras_acertadas)
    chute = input('Qual a letra?')
    posicao = 0
    for letra in palavra_secreta:


        verifica = len(palavra_secreta)
        if chute.upper() == letra.upper():
            print("Encontrei a letra {} na posição {}".format(letra, posicao))
            letras_acertadas[posicao] = letra
        posicao = posicao + 1
    if letras_acertadas == list(palavra_secreta):
        print("Parabéns você acertou!!!")
        print("Palavra: {}".format(palavra_secreta))
        acertou = True
