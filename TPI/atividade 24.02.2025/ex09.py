nomes = ["Maria", "João", "Paulo", "Magali"]
nome_procurado = input("Digite um nome para localizar: ")

for nome in nomes:
    if nome.lower() == nome_procurado.lower():
        print(f"Nome encontrado: {nome}")
        break
else:
    print("Nome não encontrado")