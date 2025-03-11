matriz = []
for i in range(5):
    linha = []
    for j in range(2):
        linha.append(int(input(f"Digite o valor da linha {i+1} e coluna {j+1}: ")))
    matriz.append(linha)

for i in range(5):
    for j in range(2):
        print(matriz[i][j],end=" ")
    print()