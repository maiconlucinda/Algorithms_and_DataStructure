
# O QUE SÃO FUNÇÕES?
    # Trechos de programa que recebem um determinado nome e podem ser chamados várias vezes durante a execusão.
    # Principais vantagens: reutilização de código, modularidade e facilidade de manutenção do sistema

# Função simples
def mensagem():
    print('Texto da função')
mensagem()
print('\n')



# Função com passagem de parametros
def mensagem2(texto):
    print(texto)
mensagem2('Maicon')

# Função com passagem de parametros
def soma(a, b):
    print(a + b)
soma(5, 7)
print('\n')



# Função com passagem de parametros e retorno
def soma2(a, b):
    return a + b
r = soma2(8, 9)
print(r)

# Função com passagem de parametros e retorno
def calcula_energia_potencial_gravitacional(m, h, g = 10):

    '''
    :param m: Massa, entrada como uma variável float
    :param h: altura, entrada como uma variável float
    :param g: aceleração gravitacional, com valor default 10
    :return: resultado da formula
    '''

    e = g * m * h
    return e
print(calcula_energia_potencial_gravitacional(30, 12))


# Maneira de ver informações sobre as funções do Python
help(calcula_energia_potencial_gravitacional)