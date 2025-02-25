# Crie uma lista vazia para armazenar os números
numeros = []

# Pergunte ao usuário quantos números ele deseja inserir

# Peça ao usuário que insira os números
for i in range(0,20):
    numero = int(input(f"Insira o número {i+1}: "))
    numeros.append(numero)

# Inicialize uma variável para contar os múltiplos de 3
contagem_multiplos = 0

# Mostre apenas os números que são múltiplos de 3
for numero in numeros:
    if numero % 3 == 0:
        print(numero)
        contagem_multiplos += 1

# Imprima a contagem de múltiplos de 3
print(f"Existem {contagem_multiplos} números múltiplos de 3 na lista.")