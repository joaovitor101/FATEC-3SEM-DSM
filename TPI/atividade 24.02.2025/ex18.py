linguagens = ["python","c#","Visual Basic","C++","Delphi","Cobol","Clipper","PHP","Java"]

nome_linguagem = input("Digite o nome de uma linguagem: ").lower()

encontrado = False

for i, linguagem in enumerate(linguagens):
    if linguagem.lower() == nome_linguagem:
        print("Linguagem encontrada!")
        encontrado = True
        posicao = i + 1
        break

if not encontrado:
    print("Linguagem não encontrada!")

print(f"A linguagem '{nome_linguagem}' está na posição {posicao} da lista.")