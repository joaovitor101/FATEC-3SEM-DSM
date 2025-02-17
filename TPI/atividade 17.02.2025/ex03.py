h1 = float(input("Digite a primeira altura: "))
h2 = float(input("Digite a segunda altura: "))
h3 = float(input("Digite a terceira altura: "))

if h1 > h2 and h1 > h3:
   if h2 > h3:
      print("Ordem decrescente: ", h1, h2, h3)
   else:
      print("Ordem decrescente: ", h1, h3, h2)
elif h2 > h1 and h2 > h3:
   if h1 > h3:
      print("Ordem decrescente: ", h2, h1, h3)
   else:
      print("Ordem decrescente: ", h2, h3, h1)
else:
   if h1 > h2:
      print("Ordem decrescente: ", h3, h1, h2)
   else:
      print("Ordem decrescente: ", h3, h2, h1)
    

