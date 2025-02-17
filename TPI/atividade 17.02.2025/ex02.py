x = int(input("Informe um numero inteiro positivo: "))

if x % 2 == 0:
    q = x * x
    print(f"O quadrado de {x} é {q}, que é par")
else:
    c = x * x * x
    print(f"O cubo de {x} é {c}, que é impar")