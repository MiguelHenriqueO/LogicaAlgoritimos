""""
##if
x = int(input("digite um número: "))

if x > 0:
    print("positivo") 
    print("fim do programa")

#else
notaA = int(input("informe a nota do aluno: "))
if notaA >= 30 and notaA <60:
    print("o aluno precisa fazer SUB")
else:
    print("o aluno está aprovado")


x = int(input("digite um número: "))
if x % 2 == 0:
    print("o número é par")
else:
    print("o numero é impar")

#Alinhamento de if
x= int(input("digite um valor inteiro: "))
if x == 0:
    print("o valor", x, " é igual a zero")
else:
    if x > 0:
        print("o valor", x, " é positivo")
    else:
        print("o valor ", x," é negativo")
print("fim do programa")
"""
#elif
x= int(input("digite um valor inteiro: "))
if x == 0:
    print("o valor", x, " é igual a zero")
elif x > 0:
    print("o valor", x, " é positivo")
else:
     print("o valor ", x," é negativo")
print("fim do programa")