nAulas = int(input("Digite o número de aulas: "))
nPresenca = int(input("Digite o número de aulas que o aluno estava presente: "))
nota = float(input("Digite a nota do aluno: "))

if nPresenca / nAulas >= 0.75 and nota >= 6:
    print("A")
elif nPresenca / nAulas >= 0.75 and nota < 6:
    print("R")
else:
    print("F")
