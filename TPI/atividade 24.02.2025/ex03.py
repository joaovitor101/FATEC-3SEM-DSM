#eu quero uma tabuada do numero que for digitado usando while

numero = int(input("Digite um número para ver sua tabuada: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1