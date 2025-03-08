valor_compra = float(input('Digite o valor da compra: '))   

if valor_compra < 20:
    lucro = valor_compra * 0.45
else:
    lucro = valor_compra * 0.30

print(f'Valor de venda: {valor_compra + lucro}')    



