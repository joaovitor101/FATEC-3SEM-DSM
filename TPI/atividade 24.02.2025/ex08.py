total_compra = 0
while True:
        preco = float(input("Digite o preço da mercadoria (0 para finalizar): "))
        if preco == 0:
            break
        total_compra += preco
print(f"Total da compra: R${total_compra:.2f}")
    
while True:
        dinheiro_fornecido = float(input("Digite o valor em dinheiro fornecido pelo cliente: "))
        if dinheiro_fornecido >= total_compra:
            print(f"Troco: R${dinheiro_fornecido - total_compra:.2f}")
            break
        else:
            print("Valor insuficiente.")