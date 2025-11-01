#1 um investidor tem 2 opções de aplicação:

# a) cdb => 14,5%
# b) lca => 11,5%
# c) poupança: 6%

#amos investimentos são por prazos fixos, com 5, ou 10 ou 20 anos. Calcule a rentabilidade ano a ano e total OBS: para CDB há imposto de enda sobre o rendimento de 15%

def calculoCDB(valor,tempo):
    rentabilidadeAnual = valor * 0.145
    total = (rentabilidadeAnual * tempo) + valor
    descontado = total - (total * 0.15)
    print("A rentabilidade anual é de: R$",rentabilidadeAnual)
    print("O total de lucro com o investimento CDB com desconto de 15% durante o tempo informado foi de: R$", descontado)

def calculoLCA(valor,tempo):
    rentabilidadeAnual = valor * 0.115
    total = (rentabilidadeAnual * tempo) + valor
    print("A rentabilidade anual é de: R$",rentabilidadeAnual)
    print("O total de lucro com investimento LCA durante o tempo informado foi de: R$", total)

def calculoPoupanca(valor,tempo):
    rentabilidadeAnual = valor * 0.06
    total = (rentabilidadeAnual * tempo) + valor
    print("A rentabilidade anual é de: R$",rentabilidadeAnual)
    print("O total de lucro com investimento Poupança durante o tempo informado foi de: R$", total) 

investido = float(input("Informe o valor investido: "))
duracao = int(input("Informe a duração do investimento (5 , 10 ou 20 anos): "))
if duracao == 5 or duracao == 10 or duracao == 20:
    aplicacao = input("informe qual será seu meio de investimento (CDB, LCA ou Poupança): ")

    if aplicacao == "CDB":
        calculoCDB(investido,duracao)
    elif aplicacao == "LCA":
        calculoLCA(investido,duracao)
    elif aplicacao == "Poupança":
        calculoPoupanca(investido,duracao)
    else:
        print("Metodo de aplicação inválido!!!")
else:
    print("Tempo de duração Inválido!!")
