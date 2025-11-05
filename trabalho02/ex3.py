moda = []

while True:
    entrada = input("Informe um número ou 'sair' para sair: ").strip().lower()

    if entrada == "sair":
        break

    try:
        num = int(entrada)
        moda.append(num)
    except ValueError:
        print("por favor informe um número ou 'sair' para finalizar o programa")

if len(moda) == 0:
    print("informe pelo menos um número")

print("números informados: ", moda)
