lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print("Maior: {}".format(max(lista)))
print("Menor: {}".format(min(lista)))
print("Pares:", end=" ")
for i in lista:
    if i % 2 == 0:
        print("{}".format(i), end=", " )

print("\nOcorrencias do primeiro elemento da lista:", end=" ")
count = 0
for i in lista:
    if i == lista[0]:
        count += 1
print("{}".format(count))

soma = 0
soma = soma + i
soma_negativa = 0
for i in lista:
    soma +=i
    if i < 0:
        soma_negativa += i
print("Média: {}".format(soma/len(lista)))
print("Soma dos valores negativos: {}".format(soma_negativa))
