j1 = str(input("Escolha pedra, papel ou tesoura: ")).lower()
j2 = str(input("Escolha pedra, papel ou tesoura: ")).lower()

if j1 == j2:
    print("Empate!")
elif (j1 == "pedra" and j2 == "tesoura") or (j1 == "papel" and j2 == "pedra") or (j1 == "tesoura" and j2 == "papel"):
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")