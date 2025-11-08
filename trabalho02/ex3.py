def modaNums(num):
    contagem = {}
    for n in num:
        contagem[n] = contagem.get(n,0) + 1

    maiorFreq = max(contagem.values())

    candidatos = []
    for num, freq in contagem.items():  
        if freq == maiorFreq:             
            candidatos.append(num)       

    if len(candidatos) == 1:
        return candidatos[0]
    else:
        return None





moda = []

qnt = int(input("Informe a quantidade de números usados para fazer a moda: "))
if qnt <= 1:
    print("não há moda")
else:
    for i in range(qnt):
        try:
            inputModa = int(input(f"informe o {i+1} número positivo da lista: "))
            if inputModa >= 0:    
                moda.append(inputModa)
        except ValueError:
            print("Valor inválido informado, informe um número positivo")
            break

    resultado = modaNums(moda)
    if resultado is None:
        print("não há moda")
    else:
        print(f"A moda é {resultado}")
    




