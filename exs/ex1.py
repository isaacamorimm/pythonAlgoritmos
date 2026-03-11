n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2

if n2 % 3 == 0:
    print(f"A soma dos números é {soma}")
else:
    print("O segundo número não é múltiplo de 3.")