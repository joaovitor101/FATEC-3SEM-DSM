



capitais = []
for i in range(2):
    linha = []  
    for j in range(3):
        linha.append(input(f"Digite o nome da capital {j+1}: "))
    capitais.append(linha)

for i in range(2):
    for j in range(3):
        print(capitais[i][j],end=" ")
    print()


