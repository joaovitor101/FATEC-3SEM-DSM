#Crie um vetor para digitar nomes de Times de Futebol , sem especificar o tamanho do vetor e mostrar os nomes dos times no final e termine quando digitar 0

times = []
while True:
    time = input("Digite o nome do time: ")
    if time == "0":
        break
    times.append(time)

print(times)











