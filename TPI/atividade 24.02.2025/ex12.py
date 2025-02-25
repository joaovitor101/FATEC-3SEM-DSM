#digite 7 nomes e armazene num array e mostre-a com sua posição usando for

nomes = []
for i in range(7):
    nomes.append(input(f"Digite o nome {i+1}: "))

print(5*"*" + "NOMES DIGITADOS " + 5*"*")
for i in range(len(nomes)):
  
    print(f"Posição {i+1}: {nomes[i]}")
