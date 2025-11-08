alunos = []
notas = []
status = []
soma = 0
aprov = 0
reprov = 0
porcAprov = 0

while True:
    opc = input("deseja adicionar um novo aluno? (sim | nao) ")
    if opc == "sim":
        nome = (input("Informe o nome do novo aluno: "))
        nota = int(input("informe a nota desse aluno: "))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            alunos.append(nome)
            if nota >= 7 and nota <=10:
                status.append("aprovado")
                aprov = aprov + 1
            elif nota <7 and nota >= 0:
                status.append("reprovado")
                reprov = reprov + 1
        else:
            print("nota informada é inválida!, informe uma nota entre 0 e 10")




    elif opc == "nao":
        break
    else:
        print("opção inválida! digite sim ou não")

for i in range(len(notas)):
    soma += notas[i]
    media = soma / len(notas)
    maior = max(notas)
    menor = min(notas)


print("A quantidade total de alunos é: ", len(alunos))
print("A média geral das notas foi de: ", media)
print("A porcentagem de alunos aprovados foi de: ", (aprov/len(alunos))*100,"%")
print("A maior nota foi de: ", maior)
print("A menor nota foi de: ", menor)
print("----Lista Alunos----")

for i in range(len(alunos)):
    print("nome aluno: ", alunos[i], "nota aluno: ", notas[i], "Status aluno: ", status[i])