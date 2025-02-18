s = float(input("Digite o salario do cara: "))
print(15*"*", "CATEGORIAS DOS FUNCIONARIOS", 15*"*")
print("Categoria A\nCategoria B\nCategoria C")
c = input("Digite a categoria do cara: ")

match c:
    case "A" | "a":
        sm = s + (s * 0.1)
        print(f"O salario atual do cara é {s}, e com aumento é {sm}")
    case "B" | "b":
        sm = s + (s * 0.15)
        print(f"O salario atual do cara é {s}, e com aumento é {sm}")
    case "C" | "c":
        sm = s + (s * 0.25)
        print(f"O salario atual do cara é {s}, e com aumento é {sm}")
    case _:
        print("Categoria invalida")