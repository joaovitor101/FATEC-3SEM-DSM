nome = input('Digite o nome do cliente: ')
deposito = float(input('Digite o valor do depósito: '))
saldoatual = 800 + deposito

if saldoatual == 0:
    print(f'Saldo Limite, {nome}, {saldoatual}')
elif saldoatual > 0:
    print(f'Saldo Positivo, {nome}, {saldoatual}')
else:
    print(f'Saldo Negativo, {nome}, {saldoatual}')

    