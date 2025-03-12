# Criando uma lista vazia para armazenar os nomes dos times
times = []

# Loop para permitir a entrada de nomes de times
while True:
    # Solicita ao usuário que digite um nome de time ou 0 para finalizar
    entrada = input("Digite o nome de um time de futebol (ou '0' para encerrar): ")

    # Se o usuário digitar '0', o loop é encerrado
    if entrada == '0':
        break

    # Adiciona o nome do time à lista, após dividir a entrada em palavras (caso o usuário queira digitar mais de um nome separado por espaço)
    times.extend(entrada.split())

# Exibe os nomes dos times digitados
print("\nTimes de Futebol digitados:")
for time in times:
    print(time)
