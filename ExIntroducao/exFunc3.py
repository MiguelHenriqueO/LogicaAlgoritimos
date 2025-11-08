def mediaAritimetica(num):
    soma = sum(num) #a func sum soma todos os números na lista
    for x in num:
        #soma = soma + x
        mediafinal = soma / len(num)
    return mediafinal

def mediaPon(num,peso):
    soma = 0
    for i in range(len(num)):
        soma += num[i] * pesos[i]
    return soma / sum(pesos)    

numeros = []
pesos = []
qnt = int(input("quantos numeros você quer usar? "))
for i in range(qnt):
    numero = int(input(f"informe o {i+1}° numero: "))
    peso = int(input(f"Informe o peso da nota {i+1} na media: "))
    numeros.append(numero)
    pesos.append(peso)

print("media aritimetica: ",mediaAritimetica(numeros))
print("media ponderada: ",mediaPon(numeros,pesos))

    
