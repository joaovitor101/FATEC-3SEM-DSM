#leia 10 numeros e separes pares e impares e printe


numeros = []
pares = []
impares = []

for _ in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números:", numeros)
print("Pares:", pares)
print("Ímpares:", impares)