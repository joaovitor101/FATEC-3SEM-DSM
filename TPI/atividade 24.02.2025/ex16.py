# Na sequência de 1 a 750 mostre os número com espaçamento de 4 em 4, e no final mostre a quantidade de número que foram mostrados na tela (UTILIZE FOR)


contagem = 0
for i in range(1, 751, 4):
    print(i)
    contagem += 1
print(f"Foram mostrados {contagem} números na tela.")



