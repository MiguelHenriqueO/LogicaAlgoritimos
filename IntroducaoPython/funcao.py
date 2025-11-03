#### Função 1

#def imprimeCompras():
#    compras = ["miojo","ovo","leite","pão"]
#   print("Lista de compras")
#    for item in compras:
#        print("produto:", item)


#print("Antes da função")

#imprimeCompras()

#print("Depois da função")

##### Função 2

#def reajuste(salario, juros =0.25):
#    return salario + salario * juros

#print("reajuste 1: ", reajuste(100))
#print("reafuste 2: ", reajuste(100,0.10))

##### Função 3

def maior(x,y):
    if x>y:
        return x 
    else:
        return y
        print("Essa mensagem não será impressa")

x= int(input("digite o valor de x: "))
y = int(input("digite o valor de y: "))
z = maior(x,y)



print("o maior valor é: ", z)

