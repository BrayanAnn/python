########## JOGO DA ADVINHAÇÃO ##########
def jogar():
    import random

    print("########## JOGO DA ADVINHAÇÃO ##########")

    #Variáveis
    level = int(input("\nSelecione o nível (1 - Fácil, 2 - Médio, 3 - Difícil):"))
    numero_secreto = random.randint(0, 100 * level) #Gera um número aleatório entre 0(zero) e 100(número base) * level

    if level > 3 or level < 1:
        print("Nível inválido")

    else:
        tentativa = 1
        while(tentativa):
            chute = int(input("Tentativa {}, Digite um número\n".format(tentativa))) #Recebe o chute do usuário (rsrsrs)
            #Variaveis condicionais
            acertou = numero_secreto == chute
            maior = numero_secreto > chute
            menor = numero_secreto < chute
            if(acertou):
                print("Você acertou, na tentativa {}".format(tentativa))
                break #Usado para interromper o loop while infinito quando o usuário advinhar o número
            elif(numero_secreto > chute):
                print("O número é maior que o chute")#Se o numero for maior imprime
                tentativa += 1 #Incrementa tentativa
            elif(numero_secreto < chute):
                print("O numero é menor que o chute")#Se o numero for menor imprime
                tentativa +=1 #Incrementa tentativa
