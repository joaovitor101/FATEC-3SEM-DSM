medida = float(input('Digite a medida em metros: '))

print('1- Decimetros')
print('2- Centimetros')
print('3- Milimetros')

opcao = int(input('Digite a opcao desejada: '))

match opcao:
    case 1:
        print(f'{medida} metros equivale a {medida * 10} decimetros')
    case 2:
        print(f'{medida} metros equivale a {medida * 100} centimetros')
    case 3:
        print(f'{medida} metros equivale a {medida * 1000} milimetros')
    case _:
        print('Opcao invalida')