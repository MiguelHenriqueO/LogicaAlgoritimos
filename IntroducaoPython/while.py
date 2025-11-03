"""""
a = int(input("digite o valor A ;"))
b = int(input("digite o valor B :"))
while a <= b:
    print(a)
    a=a+1

print("fim do programa")
"""

numero = 0
cont = 0
n = int(input("informe a quantidade de números desejada: "))
while cont < n:
    numero = numero + int(input(f"informe o {cont+1}° número: "))
    cont = cont +1

media = numero / cont
print("A média desses números é: ", media)
print("Fim programa")
