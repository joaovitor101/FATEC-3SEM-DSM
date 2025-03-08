num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
op = input('Digite a opção desejada: (+ - * /): ')

match op:
    case '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    case '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    case '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    case '/':
        print(f'{num1} / {num2} = {num1 / num2}')
    case _:
        print('Opção inválida')
