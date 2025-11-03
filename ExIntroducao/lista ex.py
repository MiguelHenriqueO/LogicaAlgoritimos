quantidade = []
valor = []
cont = 5
total = 0
mValor = 0
qntMV = 0
totalP = []

for i in range(5):
    quantidade.append(int(input(f"Quantidade do produto {i+1}: ")))
    valor.append(int(input(f"Valor do produto {i+1}: ")))
    

for i in range(len(quantidade)):
    total += quantidade[i] * valor[i]
    if valor[i] > mValor:
        mValor = valor[i]
        qntMV = quantidade[i]
    totalP.append(valor[i]*quantidade[i])
    

for i in range(len(totalP)):
    print(f"A quantidade do produto {i+1} é: {quantidade[i]}")
    print(f"O valor do produto {i+1} é: R${valor[i]}")
    print(f"O valor total da somas das unidades do produto {i+1} é: R${totalP[i]}\n")

print(f"O valor de todos os produtos foi de: R${total}\n")
print(f"O maior valor foi de: R${mValor} com {qntMV} unidades\n")



 