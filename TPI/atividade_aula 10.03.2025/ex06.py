

vetor = []
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    vetor.append(num)

for num in vetor:
    if num % 2 == 0:
        print(f"{num} é par")
