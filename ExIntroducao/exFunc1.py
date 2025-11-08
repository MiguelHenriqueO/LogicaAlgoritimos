def calcular(a,b,operacao):
    if operacao.lower() == "+":
        return a + b
    elif operacao.lower() == "-":
        return a - b
    elif operacao.lower() == "*":
        return a * b
    elif operacao.lower() == "/":
        return a / b
    else:
        print("Informe uma opção valida: subtrai, multiplica , soma ou divide")

tipoOperacao = input(f"informe o tipo de operação a ser feito: (+, - , * ou /) ").strip()
num1 = int(input("Informe o primeiro número da operação: "))
num2 = int(input("Informe o segundo número da operação: "))

resultado = calcular(num1,num2,tipoOperacao)

print(f"O resultado da operação {num1} {tipoOperacao} {num2} é: {resultado}")