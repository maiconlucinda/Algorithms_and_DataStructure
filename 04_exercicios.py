

# 1 Ler dois números inteiros, executar e mostrar o resultado das seguintes operações:
# adição, subtração, multiplicação e divisão

primeiroNumero = int(input('Insira o primeiro valor '))
segundoNumero = int(input('Insira o sefundo valor '))

print('Resultado da adição dos numeros', primeiroNumero + segundoNumero)
print('Resultado da subtração dos números', primeiroNumero - segundoNumero)
print('Resultado da multiplicação dos números', primeiroNumero * segundoNumero)
print('Resultado da divisão dos números', primeiroNumero / segundoNumero)
print('\n')






#  2 Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando
# um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo
# gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter
# a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da
# distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a
# fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,
# tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

tempoViagem = float(input('Insira por favor o tempo gasto na viagem '))
velocidadeMédia = float(input('Insira por favor a velocidade média da viagem '))


distancia = tempoViagem * velocidadeMédia
litrosUsados = distancia / 12

print('A velocidade média foi de ', velocidadeMédia)
print('O tempo gasto na viagem foi de ', tempoViagem)
print('A distancia percorrida foi de', distancia)
print('A quantidade de litros utilizada foi de ', litrosUsados)




