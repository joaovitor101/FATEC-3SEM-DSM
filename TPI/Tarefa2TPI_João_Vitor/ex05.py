nome1 = input('Digite o nome da primeira pessoa: ')
altura1 = float(input('Digite a altura da primeira pessoa: '))
idade1 = int(input('Digite a idade da primeira pessoa: '))

nome2 = input('Digite o nome da segunda pessoa: ')
altura2 = float(input('Digite a altura da segunda pessoa: '))
idade2 = int(input('Digite a idade da segunda pessoa: '))

if altura1 > altura2:
    print(f'{nome1} tem {altura1} e {idade1} anos')
else:
    print(f'{nome2} tem {altura2} e {idade2} anos')
