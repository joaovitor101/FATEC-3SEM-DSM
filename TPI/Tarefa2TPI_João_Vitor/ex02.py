medida = float(input('Digite a medida em metros: '))

print('1- decímetros 2- Centímetros 3- Milimetros')

opcao = int(input('Digite a opção desejada: '))

match opcao:
    case 1:
        print(f'{medida} metros equivale a {medida * 10} decímetros')
    case 2:
        print(f'{medida} metros equivale a {medida * 100} centímetros')
    case 3:
        print(f'{medida} metros equivale a {medida * 1000} milimetros')
    case _:
        print('Opção inválida')