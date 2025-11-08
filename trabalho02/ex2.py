alunos = []
notas = []
media = 0

while True:
    opc = input("deseja adicionar um novo aluno? (sim | nao) ")
    if opc == "sim":
        nome = (input("Informe o nome do novo aluno: "))
        nota = int(input("informe a nota desse aluno: "))
        notas.append(nota)
        alunos.append(nome)

    elif opc == "nao":
        break

    else:
        print("opção inválida! digite sim ou não")

for i in notas: 
    media += notas[i] / len(notas)

print(alunos)
print(notas)
print(media)