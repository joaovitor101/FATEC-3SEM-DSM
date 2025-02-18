x = float(input("Digite o preço final: "))
print(15*"*", "MÉTODO DE PAGAMENTO", 15*"*")
print("1 - Á vista\n2 - Cartão de débito\n3 - Cartão de crédito(Vencimento)\n")
y = int(input("Escolha o método de pagamento: "))

match y:
    case 1:
        um = x - (0.15 * x)
        print("Valor final é", um)
    case 2:
        um = x - (0.1 * x)
        print("Valor final é", um)
    case 3:
        um = x - (0.05 * x)
        print("Valor final é", um)
    case _:
        print("Opção inválida")