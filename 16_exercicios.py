#  1 -Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
# A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a
# temperatura em graus Celsius
# - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

def resultado(valor):
    print(valor)


def calculo(celsius):
    fah = (9 * celsius + 160) / 5
    resultado(fah)


def celsiustofah():
    celsius = float(input('Insira a temperatura em Celsius '))
    calculo(celsius)


celsiustofah()
print('\n')






# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz
# 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média
# durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
# Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula:
# LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem,
# a distância percorrida e a quantidade de litros utilizada na viagem
# - Função para ler os valores (não recebe parâmetro e retorna os dois valores)
# - Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
# - Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
# - Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)


# Faz 12Km com 1 litro
# Viagem levou 4h (receber via input)
# Media velocidade de 80km por hora (receber via input)


def leituraValores():
    tempoViagem = float(input('Digite o tempo gasto na viagem em horas '))
    valocidadeMedia = float(input('Digite a velocidade média da viagem '))
    return tempoViagem, valocidadeMedia



def calcularDistancia(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia


def quantidadelitros(distancia):
    return distancia / 12


def mostrarresultado(leituraValores, resultadoDistancia, quantidadeLitros):
    print('O tempo médio da viagem foi de: ', leituraValores[0], 'h, a valocidade média da viagem foi de ', leituraValores[1], 'h')
    print('A distancia percorrida na viagem foi de: ', resultadoDistancia)
    print('A quantidade de litros de combustível usado na viagem foi de: ', quantidadeLitros)




resultadoLeitura = leituraValores()
resultadoDistancia = calcularDistancia(resultadoLeitura[0], resultadoLeitura[1])
quantidadeLitros = quantidadelitros(resultadoDistancia)
mostrarresultado(resultadoLeitura, resultadoDistancia, quantidadeLitros)

