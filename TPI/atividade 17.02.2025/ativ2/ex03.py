<<<<<<< HEAD
print(5*"*", "CALCULO DE GRANDEZAS ELÉTRICAS", 5*"*")

print("1 - Valor da tensão\n2 - Valor da corrente\n3 - Valor da resistência")
opcao = float(input("Digite o valor da opção desejada: "))

match opcao:
    case 1:
        r = float(input("Digite o valor da resistencia: "))
        i = float(input("Digite o valor da corrente: "))
        u = r*i
        print(f"O valor da tensão é {u}V")
    case 2:
        r = float(input("Digite o valor da resistencia: "))
        u = float(input("Digite o valor da tensão: "))
        i = u/r
        print(f"O valor da corrente é {i}A")
    case 3:
        u = float(input("Digite o valor da tensão: "))
        i = float(input("Digite o valor da corrente: "))
        r = u/i
        print(f"O valor da resistencia é {r}Ω")
    case _:
=======
print(5*"*", "CALCULO DE GRANDEZAS ELÉTRICAS", 5*"*")

print("1 - Valor da tensão\n2 - Valor da corrente\n3 - Valor da resistência")
opcao = float(input("Digite o valor da opção desejada: "))

match opcao:
    case 1:
        r = float(input("Digite o valor da resistencia: "))
        i = float(input("Digite o valor da corrente: "))
        u = r*i
        print(f"O valor da tensão é {u}V")
    case 2:
        r = float(input("Digite o valor da resistencia: "))
        u = float(input("Digite o valor da tensão: "))
        i = u/r
        print(f"O valor da corrente é {i}A")
    case 3:
        u = float(input("Digite o valor da tensão: "))
        i = float(input("Digite o valor da corrente: "))
        r = u/i
        print(f"O valor da resistencia é {r}Ω")
    case _:
>>>>>>> 5df28f7027fccff3fc6f4b354b1b22c6d99287de
        print("Opção inválida. Por favor, tente novamente.")