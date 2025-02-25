multiplicador = int(input("Digite a tabuada que oce ira calcular: "))
inicial = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))

print(f"Tabuada de: {multiplicador}")
print("Tabuada:")
while inicial <= final:
    print(f"{multiplicador} x {inicial} = {multiplicador * inicial}")
    inicial += 1