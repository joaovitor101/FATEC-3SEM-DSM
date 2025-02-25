nomes = ["Luiz", "Ana", "Cristina", "Fernanda", "Maria Alice", "Joaquina"]

while True:
    escolha = input("Digite 1 para buscar um nome ou 0 para sair: ")
    
    if escolha == "1":
        nome_busca = input("Digite um nome para localizar: ")
        
        for nome in nomes:
            if nome.lower() == nome_busca.lower():
                print(f"Nome encontrado: {nome}")
                break
        else:
            print("Nome não encontrado")
    elif escolha == "0":
        print("Saindo da aplicação...")
        break
    else:
        print("Opção inválida. Tente novamente.")