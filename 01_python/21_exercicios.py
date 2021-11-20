

list = []
try:
    list.append(float(input('Insira o primeiro valor: ')))
    list.append(float(input('Insira o segundo valor: ')))

    divisao = list[0] / list[1]
except ValueError:
    print('Valor inválido')
except ZeroDivisionError:
    print('O segundo valor precisa ser diferente de Zero')
except KeyboardInterrupt:
    print('O usuário interrompeu a execução')
else:
    print(f'A divisão é {divisao}')




