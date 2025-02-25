linguagens = ["python","c#","Visual Basic","C++","Delphi","Cobol"]

# Mostrar somente as linguagens que possuem mais de 3 caracteres
for linguagem in linguagens:
    if len(linguagem) > 3:
        print(linguagem)

# Mostrar a quantidade de caracteres de todas as linguagens da lista
print("\nQuantidade de caracteres de cada linguagem:")
for linguagem in linguagens:
    print(f"{linguagem}: {len(linguagem)}")