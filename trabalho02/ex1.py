def desconto(idade,valor):
    desconto = 0.0
    if valor > 200 and valor <=500:
        print(f"o desconto base para essa compra é de: R${valor*0.10}")
        if idade < 25:
            desconto = valor * 0.15
            print(f"você está apto ao desconto adicional no valor de: R${desconto}")
        elif idade >= 60:
            desconto = valor * 0.17
            print(f"você está apto ao desconto adicional no valor de: R${desconto}")
        else:
            desconto = valor * 0.10

    elif valor > 500:
        print(f"o desconto base para essa compra é de: R${valor*0.15}")
        if idade < 25:
            desconto = valor * 0.20
            print(f"você está apto ao desconto adicional no valor de: R${desconto}")
        elif idade >= 60:
            desconto = valor * 0.22
            print(f"você está apto ao desconto adicional no valor de: R${desconto}")
        else:
            desconto = valor * 0.15
    else:
        if idade < 25:
            desconto = valor * 0.05
            print(f"você está apto ao desconto adicional no valor de: R${desconto}")
        elif idade >= 60:
            desconto = valor * 0.07
            print(f"você está apto ao desconto adicional no valor de: R${desconto}")


    return desconto




idadeCliente = int(input("Informe a sua idade: "))
valorTotal = int(input("Informe o valor total da compra: "))

descontoF = desconto(idadeCliente, valorTotal)

print(f"O valor final da sua compra será de: R${valorTotal-descontoF}")


