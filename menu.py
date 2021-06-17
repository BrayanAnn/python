import forca
import advinhacao

print("###########################")
print("###### MENU DE JOGOS ######")
print("###########################")
print("1 - Jogo da advinhação")
print("2 - Jogo da forca")

escolha = int(input("Digite o número do jogo que deseja jogar"))

if escolha == 1:
    advinhacao.jogar()
elif escolha == 2:
    forca.jogar()