nota = int(input("informe qual foi sua nota: "))

if nota >= 30 and nota < 60:
    print("a nota do aluno é de", nota, "e ele precisara fazer sub")
elif nota < 30:
    print("a nota do aluno é de", nota, "e ele está reprovado")
else:
    print("a nota do aluno é de", nota, "e ele não precisara fazer sub")