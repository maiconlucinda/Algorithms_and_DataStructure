
# Erros mais comuns que podem aparecer quando estamos trabalhando com Python

# NameError: variável não foi definida
# TypeError: tipos de dados incompatíveis
# RuntimeError: erro de execução
# SyntaxError: sintaxe digitada é inválida e não reconhecida pelo interpretador
# ZeroDivisionError: divisão por zero
# IndexError: índice está fora da coleção





# O computador é burro, então devemos programar exatamente o que ele deve fazer, devemos até mesmo programar como ele deve
# se comportar caso algo inesperado aconteca, isso é exatamente pelo fato dele ser uma máquina que só faz o que é programado
# para ser feito, se não houver instruções para deterinada situação, é impossível essa máquina saber o que deve ser feito.
# Em situações assim, utilizamos exceções, para que quando acontecer algo no nosso código que é fora do que era esperado
# o sistema saiba se comportar também.

try:
    # Tente fazer isso, caso não seja possível, lance uma excessão, daí o except saberá qual instrução seguir.
    n = int(input('Digite um número inteiro: '))
except:
    print('Valor Inválido')

else:
    print(f'Valor digitado é: {n}')





# Que tal fazermos a execução do código try except toda vez que a informação ser inserida incorretamente?
import time
while True:
    try:
        n = int(input('Digite sua idade: ' ))
        time.sleep(1)
    except:
        time.sleep(1)
        print('Idade inválida ', '\n')
        print('Por favor insira uma idade válida ')
    else:
        print(f'Sua idade é: {n}')
        break



# Quando só fazemos except, estamos pegando qualquer tipo de erros, mas podemos também pegar um determinado tipo de erro
while True:
    try:
        p = int(input('Insira o ano que voce nasceu: '))
    except ValueError:
        print('Valor inválido')
    except KeyboardInterrupt:
        print('\n')
        print('Usuário interrompeu a execução') # A máquina não tem instruções de que em um determinado momento o usuáio irá
                                                # interromper o código, então isso também é uma excecção, daí quando o usuário
                                                # presciona a opção de parar a execução, é lancada uma exceção justamente porque
                                                # por padrão não é algo que está no código, logo, o computador não sabe lidar com isso.
        break
    else:
        print(f'Valor digitado é: {p}')



