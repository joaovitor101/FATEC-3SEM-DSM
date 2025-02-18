x = input("Digite alguma letra: ")

match x:
    case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' | 'U':
        print("Voce escolheu uma vogal")
    case _:
        print("Voce digitou uma consoante")

