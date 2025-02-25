funcionarios = []

for i in range(2):
    nome = input("Digite o nome do funcionário: ")
    sexo = input("Digite o sexo do funcionário (M/F): ").upper()
    
    while sexo not in ['M', 'F']:
        print("Sexo digitado incorretamente. Por favor, digite M ou F.")
        sexo = input("Digite o sexo do funcionário (M/F): ").upper()
    
    funcionarios.append({'nome': nome, 'sexo': sexo})

for funcionario in funcionarios:
    if funcionario['sexo'] == 'M':
        print(f"Nome: {funcionario['nome']}, Necessita fazer o exame: Sim")
    else:
        print(f"Nome: {funcionario['nome']}, Necessita fazer o exame: Não")