compras = ["arroz", "carne", "feijão", 12.2]

#print(compras)

#print(list(range (5)))

#print(compras[3])

#print(len(compras))

#lista = [1.2, 2.3, 3.5, 6.6, 7.7]

#soma = 0

#for n in lista:
#    soma += n

#print("soma das notas: ", soma)

#lista posicional

#for n in range(len(compras)):
#    print(f"posição {n} da lista: {compras[n]}")


n = 5
notas = []
for i in range(1, n+1):
    x = int(input("nota do aluno: "))
    notas.append(x)

media = 0
for n1 in notas:
    media = media +n1

media = media /n

for n1 in notas:
    if n1 > media:
        print("Aprovado: ",n1)

print(media)


