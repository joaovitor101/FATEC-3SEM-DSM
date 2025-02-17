n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

x = print("1 - Media Ponderada\n2 - Quadrado da soma\n3 - Cubo do menor número")

x = int(input("Escolha uma opção: "))

if x == 1:
    media = (n1 * 2 + n2 * 3) / (2+3)
    print("A media ponderada é: ", media)
elif x == 2:
        print("O quadrado da soma é: ", (n1 + n2) ** 2)
elif x == 3:
        menor = min(n1, n2)
        print("O cubo do menor número é: ", menor ** 3)
else:
       print("Opção invalida")
    