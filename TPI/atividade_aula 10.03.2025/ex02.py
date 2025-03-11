matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input(f"Digite o valor da linha {i+1} e coluna {j+1}: ")))
    matriz.append(linha)

for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            print("os valores maiores que 10: ",matriz[i][j])