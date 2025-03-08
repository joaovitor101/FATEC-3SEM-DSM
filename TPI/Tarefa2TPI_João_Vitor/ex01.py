ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade >= 16:
    print('Pode votar')
else:
    print('Nao pode votar')
