#crie um programa que controle vendas e solivite ao usuario: nome produt, valor, quantidado, método de pagamento (1- a vista, 2- a prazo), se a prazo solicite n° de parcelas e, calcule total: 
# -a vista = desconto 10%
# a prazo = acréscimo de (15% até 5 parcelas, 20% acima de 5, calcule  mostr, total de venda, desconto, liquido a pagar, se a prazo, mostre valor de cada parcela.)

nomeProduto = input("iforme o nome do produto: ")
valorProd = float(input("\ninforme o valor do produto: "))
if(valorProd > 0):
    qnt = int(input("\nInforme a quantidade comprada: "))
    if(qnt > 0):
        metodoPag = input("\nInforme o método de pagamento (1- a vista, 2- a prazo): ")
        totalVenda= 0
        desconto = 0
        parcelas = 0
        aPagar = 0
        valorParcelas = 0
        acrescimo = 0

        totalVenda = valorProd * qnt

        if(metodoPag == "1"):
            aPagar = totalVenda * 0.10
            desconto = totalVenda * 0.90
            print("\nO valor total da compra foi de", totalVenda)
            print("\nO valor total a pagar foi de R$", aPagar)
            print("\nO desconto total foi de R$", desconto)
        elif(metodoPag == "2"):
            parcelas = int(input("\nInforme o número de parcelas: "))
            if(parcelas < 1):
                print("O valor de parcelas é inválido")
            elif(parcelas <= 5):
                aPagar = 0.15 * totalVenda
                valorParcelas = aPagar/parcelas
                acrescimo = 0.15 * totalVenda
                print("\nO valor de cada parcela é de R$", valorParcelas)
                print("\nO acrescimo total foi de R$", acrescimo)
                print("\nO valor total pago foi de R$", aPagar)
            elif(parcelas > 5):
                aPagar = 0.20 * totalVenda
                valorParcelas = aPagar/parcelas
                acrescimo = 0.20 * totalVenda
                print("\nO valor de cada parcela é de R$", valorParcelas)
                print("\nO acrescimo total foi de R$", acrescimo)
                print("\nO valor total pago foi de R$", aPagar)
        else:
            print("\nO código informado é inválido")
    else:
        print("\nA quantidade não pode ser nula")
else:
    print("\nO valor não pode ser nulo")
        


    