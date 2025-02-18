x = int(input("Digite o indice de poluição: "))

match x:
    case 0 | 1 | 2 :
        print("Aceitável")
    case 3 | 4 | 5 :
        print("Suspender atividades grupo 1")
    case 6 | 7 :
        print("Suspender atividades grupo 1 e 2")
    case _:
        print("Suspender atividades de todos os grupos")