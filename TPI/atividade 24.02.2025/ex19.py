vogais = ['a', 'e', 'i', 'o', 'u']

for _ in range(10):
    letra = input("Digite uma letra: ").lower()
    if letra in vogais:
        print(f"A letra '{letra}' é uma vogal.")
    else:
        print(f"A letra '{letra}' não é uma vogal.")