# Cria a matriz com 5 linhas e 2 colunas
matriz = []

# Lê os dados dos produtos e suas quantidades
for i in range(5):
    produto = input(f"Digite o nome do produto {i+1}: ")
    quantidade = int(input(f"Digite a quantidade do produto {i+1}: "))
    matriz.append([produto, quantidade])

# Exibe a matriz com os produtos e suas quantidades
print("\nMatriz de produtos e quantidades:")
for i in range(5):
    print(f"Produto: {matriz[i][0]}, Quantidade: {matriz[i][1]}")
