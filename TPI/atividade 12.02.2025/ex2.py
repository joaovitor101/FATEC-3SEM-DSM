vp = float(input("Digite o valor da prestação: "))
tj = float(input("Digite a taxa de juros: "))
t = int(input("Digite o tempo em meses de atraso: "))
va = vp + (vp * (tj/100) * t)

print(f"O valor total a ser pago é {va}")
