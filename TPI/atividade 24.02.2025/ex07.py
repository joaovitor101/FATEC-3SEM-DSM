
preco_pao = 0.54

print("Tabela de preços de pães (somente quantidades pares):")
for i in range(2, 51, 2):
        preco_total = preco_pao * i
        print(f"{i} pães: R$ {preco_total:.2f}")

