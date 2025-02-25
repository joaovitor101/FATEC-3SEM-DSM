pontuacao = 0


i = 0
while i < 3:
    if i == 0:
        print("Questão 1: Qual é a cor do céu?")
        print("A) Azul")
        print("B) Verde")
        print("C) Amarelo")
        print("D) Vermelho")
        resposta = input("Resposta: ").upper()
        if resposta == "A":
            pontuacao += 1
    elif i == 1:
        print("Questão 2: Qual é o planeta mais próximo do Sol?")
        print("A) Terra")
        print("B) Marte")
        print("C) Mercúrio")
        print("D) Vênus")
        resposta = input("Resposta: ").upper()
        if resposta == "C":
            pontuacao += 1
    elif i == 2:
        print("Questão 3: Qual é o maior planeta do nosso sistema solar?")
        print("A) Terra")
        print("B) Saturno")
        print("C) Júpiter")
        print("D) Urano")
        resposta = input("Resposta: ").upper()
        if resposta == "C":
            pontuacao += 1
    i += 1

print(f"Sua pontuação é: {pontuacao}")